# よく使う GitHub Actions

## セットアップ系

| アクション | 用途 |
| ---------- | ---- |
| `actions/checkout@v4` | リポジトリのチェックアウト |
| `actions/setup-node@v4` | Node.js セットアップ |
| `actions/setup-python@v5` | Python セットアップ |
| `actions/setup-go@v5` | Go セットアップ |
| `actions/setup-java@v4` | Java セットアップ |

## キャッシュ系

| アクション | 用途 |
| ---------- | ---- |
| `actions/cache@v4` | 汎用キャッシュ |

### npm キャッシュ例

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```

## デプロイ系

| アクション | 用途 |
| ---------- | ---- |
| `amondnet/vercel-action@v25` | Vercel デプロイ |
| `aws-actions/configure-aws-credentials@v4` | AWS 認証 |
| `google-github-actions/auth@v2` | GCP 認証 |

## Docker 系

| アクション | 用途 |
| ---------- | ---- |
| `docker/login-action@v3` | Docker レジストリログイン |
| `docker/build-push-action@v5` | イメージビルド・プッシュ |
| `docker/setup-buildx-action@v3` | BuildX セットアップ |

## セキュリティ系

| アクション | 用途 |
| ---------- | ---- |
| `github/codeql-action/init@v3` | CodeQL 初期化 |
| `github/codeql-action/analyze@v3` | CodeQL 分析 |
