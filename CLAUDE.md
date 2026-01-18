# Claude Skills Template

このリポジトリは Claude Code 用のスキルテンプレート集です。

## 使い方

1. `.claude/skills/` を新規プロジェクトにコピー
2. 各スキルのテンプレート（`.tpl`）をプロジェクトに合わせてカスタマイズ

## 含まれるスキル

### コード生成

| スキル | 用途 |
| ------ | ---- |
| `generate-component` | React コンポーネントとテストを生成 |
| `generate-docs` | README、PR説明文、ADR を生成 |
| `create-skill` | 新しいスキルを作成 |
| `test-generate` | ユニットテスト・統合テストを生成 |

### コード品質

| スキル | 用途 |
| ------ | ---- |
| `code-review` | コードレビュー（正確性、可読性、保守性） |
| `security-audit` | セキュリティ監査（OWASP Top 10 ベース） |
| `refactoring` | リファクタリング（コードスメル解消） |
| `debug-helper` | デバッグ支援（根本原因の特定） |

### 設計・インフラ

| スキル | 用途 |
| ------ | ---- |
| `api-design` | REST/GraphQL API 設計 |
| `db-migration` | DB マイグレーション作成 |
| `ci-cd-setup` | GitHub Actions CI/CD 構築 |

## カスタマイズのポイント

- `SKILL.md` の `description` は Claude の自動選択に使われるため、明確なキーワードを含める
- テンプレート内の `{{placeholder}}` を実際の値に置き換える
- プロジェクト固有のパターンに合わせてテンプレートを調整
