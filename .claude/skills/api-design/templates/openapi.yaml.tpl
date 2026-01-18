openapi: 3.0.3
info:
  title: {{api_title}}
  description: {{api_description}}
  version: 1.0.0

servers:
  - url: {{base_url}}
    description: {{server_description}}

paths:
  /{{resource}}:
    get:
      summary: {{resource}}の一覧取得
      tags:
        - {{resource}}
      parameters:
        - name: page
          in: query
          schema:
            type: integer
            default: 1
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/{{Resource}}'
                  meta:
                    $ref: '#/components/schemas/PaginationMeta'
    post:
      summary: {{resource}}の作成
      tags:
        - {{resource}}
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Create{{Resource}}Request'
      responses:
        '201':
          description: 作成成功
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/{{Resource}}'
        '400':
          $ref: '#/components/responses/BadRequest'
        '422':
          $ref: '#/components/responses/ValidationError'

  /{{resource}}/{id}:
    get:
      summary: {{resource}}の取得
      tags:
        - {{resource}}
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: 成功
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/{{Resource}}'
        '404':
          $ref: '#/components/responses/NotFound'

components:
  schemas:
    {{Resource}}:
      type: object
      properties:
        id:
          type: string
        createdAt:
          type: string
          format: date-time
        updatedAt:
          type: string
          format: date-time

    Create{{Resource}}Request:
      type: object
      required: []
      properties: {}

    PaginationMeta:
      type: object
      properties:
        page:
          type: integer
        limit:
          type: integer
        total:
          type: integer

    Error:
      type: object
      properties:
        error:
          type: object
          properties:
            code:
              type: string
            message:
              type: string

  responses:
    BadRequest:
      description: リクエスト不正
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
    NotFound:
      description: リソース未発見
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
    ValidationError:
      description: バリデーションエラー
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
