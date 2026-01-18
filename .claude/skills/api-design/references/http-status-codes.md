# HTTP ステータスコード一覧

## 2xx 成功

| コード | 名前 | 用途 |
| ------ | ---- | ---- |
| 200 | OK | GET, PUT の成功 |
| 201 | Created | POST で作成成功 |
| 204 | No Content | DELETE の成功、レスポンスなし |

## 4xx クライアントエラー

| コード | 名前 | 用途 |
| ------ | ---- | ---- |
| 400 | Bad Request | リクエスト形式が不正 |
| 401 | Unauthorized | 認証エラー（トークンなし/無効） |
| 403 | Forbidden | 権限エラー（認証済みだがアクセス不可） |
| 404 | Not Found | リソースが存在しない |
| 405 | Method Not Allowed | HTTP メソッドが許可されていない |
| 409 | Conflict | リソースの競合（重複など） |
| 422 | Unprocessable Entity | バリデーションエラー |
| 429 | Too Many Requests | レート制限超過 |

## 5xx サーバーエラー

| コード | 名前 | 用途 |
| ------ | ---- | ---- |
| 500 | Internal Server Error | サーバー内部エラー |
| 502 | Bad Gateway | 上流サーバーからの不正な応答 |
| 503 | Service Unavailable | サービス一時停止 |
| 504 | Gateway Timeout | 上流サーバーのタイムアウト |
