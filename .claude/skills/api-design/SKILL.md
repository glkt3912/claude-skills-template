---
name: api-design
description: REST/GraphQL API を設計する。「API設計」「エンドポイント設計」「API仕様を作成」などの依頼時に使用。
---

# 目的

RESTful または GraphQL の API を設計し、仕様書を作成する。

# 手順

1. **要件の整理**
   - 必要なリソース・操作を洗い出し
   - クライアントの利用パターンを想定

2. **設計方針の決定**
   - REST vs GraphQL の選択
   - 認証方式（JWT, OAuth, API Key）
   - バージョニング戦略

3. **エンドポイント設計**
   - `templates/openapi.yaml.tpl` をベースに作成
   - `references/http-status-codes.md` を参照

# REST 設計原則

| 原則 | 説明 |
| ---- | ---- |
| リソース指向 | 名詞を使用（`/users`） |
| HTTP メソッド | GET, POST, PUT, DELETE |
| 一貫性 | 命名規則、レスポンス形式を統一 |

# レスポンス形式

```json
{
  "data": { ... },
  "meta": { "page": 1, "total": 100 }
}
```

# エラーレスポンス形式

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "入力値が不正です"
  }
}
```

# 参照

- `templates/openapi.yaml.tpl` - OpenAPI テンプレート
- `references/http-status-codes.md` - ステータスコード一覧

# 制約

- RESTful の原則に従う
- 過度な設計を避け、YAGNI を意識
- クライアント視点で使いやすさを重視
