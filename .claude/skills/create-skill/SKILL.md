---
name: create-skill
description: 新しいスキルを作成する。「スキルを作りたい」「新しいスキルが必要」などの依頼時に使用。
---

# 目的

Claude Code 用の新しいスキル（SKILL.md + 関連ファイル）を作成する。

# 手順

1. **スキルの目的を明確化**
   - 何を自動化・効率化したいか
   - どのようなトリガーで呼び出されるべきか

2. **ディレクトリ作成**
   ```
   .claude/skills/{{skill-name}}/
   ├── SKILL.md
   └── templates/      # 必要に応じて
   ```

3. **SKILL.md の作成**
   - `templates/skill-template/SKILL.md.tpl` を参照
   - frontmatter（name, description）を適切に設定
   - description は自動選択のキーとなるため、明確なキーワードを含める

4. **検証**
   - スキルが正しく認識されるか確認
   - 想定通りのタイミングで呼び出されるか確認

# 制約

- description は Claude が自動選択に使う重要な要素
  - 「〜の時に使用」という形式で明示する
  - 曖昧な表現を避け、具体的なキーワードを含める
- SKILL.md は 500行以下を目安に
- 詳細資料は別ファイル（reference.md など）に分離

# テンプレート

`templates/skill-template/SKILL.md.tpl` を参照。

# 使用例

```
ユーザー: データベースマイグレーション用のスキルを作って
実行: テンプレートを基に db-migration スキルを作成
```
