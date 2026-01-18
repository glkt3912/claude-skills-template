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

2. **ワークフロー設計**
   - トリガー条件（push, PR, スケジュール）
   - ジョブの依存関係

3. **ワークフロー作成**
   - `templates/` のテンプレートを参照
   - `.github/workflows/` にファイル作成

# 参照

- `templates/github-actions-ci.yaml.tpl` - CI ワークフロー
- `templates/github-actions-deploy.yaml.tpl` - デプロイワークフロー
- `references/common-actions.md` - よく使うアクション一覧

# セキュリティ考慮事項

| 項目 | 対策 |
| ---- | ---- |
| シークレット | GitHub Secrets を使用 |
| 権限 | 最小権限の原則 |
| 依存関係 | Dependabot で監視 |

# 制約

- シークレットはハードコードしない
- 長時間実行ジョブは分割を検討
- 並列実行可能なジョブは並列化
