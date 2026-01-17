# Claude Skills Template

このリポジトリは Claude Code 用のスキルテンプレート集です。

## 使い方

1. `.claude/skills/` を新規プロジェクトにコピー
2. 各スキルのテンプレート（`.tpl`）をプロジェクトに合わせてカスタマイズ

## 含まれるスキル

| スキル | 用途 |
| ------ | ---- |
| `generate-component` | React コンポーネントとテストを生成 |
| `generate-docs` | README、PR説明文、ADR を生成 |
| `create-skill` | 新しいスキルを作成 |

## カスタマイズのポイント

- `SKILL.md` の `description` は Claude の自動選択に使われるため、明確なキーワードを含める
- テンプレート内の `{{placeholder}}` を実際の値に置き換える
- プロジェクト固有のパターンに合わせてテンプレートを調整
