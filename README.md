# Claude Skills Template

Claude Code 用のスキルテンプレートです。

## 使い方

### テンプレートとして使用

1. 「Use this template」ボタンをクリック
2. 新しいリポジトリを作成
3. 各スキルをプロジェクトに合わせてカスタマイズ

### 既存プロジェクトにコピー

```bash
cp -r .claude/skills/ your-project/.claude/skills/
```

## 含まれるスキル

### コード生成

| スキル | 用途 |
| ------ | ---- |
| `generate-component` | React コンポーネントとテストを生成 |
| `generate-docs` | README、PR説明文、ADR を生成 |
| `create-skill` | 新しいスキルを作成（検証スクリプト付き） |
| `test-generate` | ユニットテスト・統合テストを生成 |

### コード品質

| スキル | 用途 |
| ------ | ---- |
| `code-review` | コードレビュー |
| `security-audit` | セキュリティ監査（OWASP Top 10） |
| `refactoring` | リファクタリング |
| `architecture-guard` | アーキテクチャ品質検証 |

### デバッグ・調査

| スキル | 用途 |
| ------ | ---- |
| `debug-helper` | デバッグ支援 |
| `log-analysis` | ログ・スタックトレース解析 |
| `performance-analysis` | パフォーマンス調査 |

### 設計・インフラ

| スキル | 用途 |
| ------ | ---- |
| `api-design` | REST/GraphQL API 設計 |
| `db-migration` | DB マイグレーション作成 |
| `ci-cd-setup` | GitHub Actions CI/CD 構築 |

### Git ワークフロー

| スキル | 用途 |
| ------ | ---- |
| `commit` | コミットメッセージ生成（英語） |
| `pr` | Pull Request 作成（日本語） |

## スキルの構造

```
.claude/skills/skill-name/
├── SKILL.md          # 必須: メタデータと指示
├── references/       # 任意: 参照ドキュメント
├── templates/        # 任意: テンプレートファイル
└── scripts/          # 任意: 実行スクリプト
```

## カスタマイズ

### description の書き方

`description` は Claude がスキルを自動選択する際の判断基準です。

```yaml
---
name: my-skill
description: |
  〇〇を実行する。
  「トリガーワード1」「トリガーワード2」などの依頼時に使用。
---
```

### Progressive Disclosure

詳細情報は `references/` や `templates/` に分離し、必要時のみ読み込みます。

## ドキュメント

- [Skills 完全ガイド](docs/skills-guide.md)

## ライセンス

MIT
