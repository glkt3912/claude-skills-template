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
   ```bash
   python scripts/init_skill.py <skill-name> --path .claude/skills
   ```

3. **SKILL.md の編集**
   - `templates/skill-template/SKILL.md.tpl` を参照
   - frontmatter（name, description）を適切に設定
   - description は自動選択のキーとなるため、明確なキーワードを含める

4. **検証**
   ```bash
   python scripts/quick_validate.py .claude/skills/<skill-name>
   ```

5. **パッケージ化（配布時）**
   ```bash
   python scripts/package_skill.py .claude/skills/<skill-name> --output ./dist
   ```

# ツール

| スクリプト | 用途 |
| ---------- | ---- |
| `scripts/init_skill.py` | テンプレートディレクトリを自動生成 |
| `scripts/quick_validate.py` | SKILL.md の構文・構造を検証 |
| `scripts/package_skill.py` | .skill ファイル（ZIP）にパッケージ |

# init_skill.py

新しいスキルのディレクトリ構造を自動生成。

```bash
python scripts/init_skill.py my-new-skill --path .claude/skills
```

生成される構造:
```
my-new-skill/
├── SKILL.md          # テンプレート付き
├── scripts/
├── templates/
└── references/
```

# quick_validate.py

SKILL.md の構文エラーを事前チェック。

```bash
python scripts/quick_validate.py .claude/skills/my-skill
```

検証項目:
- frontmatter の存在と形式
- name フィールド（64文字以下、小文字・数字・ハイフン）
- description フィールド（1024文字以下）
- 本文の行数（500行以下を推奨）

# package_skill.py

スキルを配布可能な形式にパッケージ化。

```bash
python scripts/package_skill.py .claude/skills/my-skill --output ./dist
```

出力: `my-skill-20260118.skill`（ZIP形式）

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
実行:
  1. python scripts/init_skill.py db-migration --path .claude/skills
  2. SKILL.md を編集
  3. python scripts/quick_validate.py .claude/skills/db-migration
```
