# よくあるエラーパターン

## JavaScript / TypeScript

| パターン | 原因 | 対処 |
| -------- | ---- | ---- |
| `Cannot read property 'x' of undefined` | null/undefined アクセス | オプショナルチェーン `?.` |
| `Cannot read property 'x' of null` | null アクセス | null チェック |
| `x is not a function` | 型の誤り | 型確認、呼び出し元確認 |
| `Maximum call stack size exceeded` | 無限再帰 | 再帰の終了条件確認 |
| `Unhandled Promise Rejection` | 未捕捉の Promise エラー | try/catch, .catch() |

## ネットワーク

| パターン | 原因 | 対処 |
| -------- | ---- | ---- |
| `ECONNREFUSED` | 接続先が応答しない | サービス起動確認 |
| `ETIMEDOUT` | タイムアウト | タイムアウト値調整 |
| `ENOTFOUND` | DNS 解決失敗 | ホスト名確認 |
| `ECONNRESET` | 接続がリセット | リトライ実装 |

## HTTP ステータス

| コード | 原因 | 対処 |
| ------ | ---- | ---- |
| 400 | リクエスト形式不正 | リクエストボディ確認 |
| 401 | 認証エラー | トークン有効期限確認 |
| 403 | 権限エラー | 権限設定確認 |
| 404 | リソース未発見 | URL, ID 確認 |
| 429 | レート制限 | リトライ、頻度調整 |
| 500 | サーバー内部エラー | サーバーログ確認 |
| 502 | Bad Gateway | 上流サーバー確認 |
| 503 | サービス停止 | サービス状態確認 |

## データベース

| パターン | 原因 | 対処 |
| -------- | ---- | ---- |
| `Duplicate entry` | ユニーク制約違反 | 既存データ確認 |
| `Foreign key constraint fails` | 外部キー制約違反 | 参照先データ確認 |
| `Deadlock found` | デッドロック | トランザクション順序見直し |
| `Connection refused` | 接続失敗 | DB サーバー確認 |

## システム

| パターン | 原因 | 対処 |
| -------- | ---- | ---- |
| `ENOMEM` | メモリ不足 | メモリリーク調査 |
| `ENOSPC` | ディスク容量不足 | 不要ファイル削除 |
| `EMFILE` | ファイルディスクリプタ枯渇 | ファイル閉じ忘れ確認 |
