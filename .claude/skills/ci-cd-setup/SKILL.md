---
name: ci-cd-setup
description: CI/CD パイプラインを構築する。「CI設定」「GitHub Actions作成」「デプロイ自動化」などの依頼時に使用。
---

# 目的

GitHub Actions を使用した CI/CD パイプラインを構築する。

# 手順

1. **要件の確認**
   - ビルド/テスト/デプロイの対象
   - 実行環境（Node.js バージョン等）
   - シークレット/環境変数

2. **ワークフロー設計**
   - トリガー条件（push, PR, スケジュール）
   - ジョブの依存関係
   - キャッシュ戦略

3. **ワークフロー作成**
   - `.github/workflows/` にファイル作成
   - 必要なシークレットを確認

4. **検証**
   - ドライランまたは実行テスト

# 標準ワークフロー構成

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm run lint
      - run: npm run test
      - run: npm run build
```

# よく使うアクション

| アクション | 用途 |
| ---------- | ---- |
| `actions/checkout@v4` | リポジトリのチェックアウト |
| `actions/setup-node@v4` | Node.js セットアップ |
| `actions/setup-python@v5` | Python セットアップ |
| `actions/cache@v4` | 依存関係のキャッシュ |
| `docker/build-push-action@v5` | Docker イメージのビルド・プッシュ |

# キャッシュ戦略

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```

# デプロイ例（Vercel）

```yaml
deploy:
  needs: build
  runs-on: ubuntu-latest
  if: github.ref == 'refs/heads/main'
  steps:
    - uses: actions/checkout@v4
    - uses: amondnet/vercel-action@v25
      with:
        vercel-token: ${{ secrets.VERCEL_TOKEN }}
        vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
        vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
        vercel-args: '--prod'
```

# セキュリティ考慮事項

| 項目 | 対策 |
| ---- | ---- |
| シークレット | GitHub Secrets を使用、ログに出力しない |
| 権限 | 最小権限の原則（`permissions` で制限） |
| 依存関係 | Dependabot で脆弱性監視 |
| サードパーティアクション | SHA でバージョン固定を検討 |

# 制約

- シークレットはハードコードしない
- 長時間実行ジョブは分割を検討
- 並列実行可能なジョブは並列化
