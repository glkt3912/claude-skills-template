#!/usr/bin/env python3
"""
スキルのテンプレートディレクトリを自動生成するスクリプト

使用方法:
    python init_skill.py <skill-name> [--path <output-path>]

例:
    python init_skill.py my-new-skill
    python init_skill.py my-new-skill --path .claude/skills
"""

import argparse
import os
import sys
from pathlib import Path


SKILL_MD_TEMPLATE = '''---
name: {name}
description: |
  このスキルの説明を記述。
  「トリガーワード1」「トリガーワード2」などの依頼時に使用。
---

# 目的

[このスキルが何を達成するか]

# 手順

1. **ステップ1**
   [詳細]

2. **ステップ2**
   [詳細]

# 制約

- [制約1]
- [制約2]

# 使用例

```
ユーザー: [依頼例]
実行: [実行内容]
```
'''


def create_skill_directory(skill_name: str, base_path: str = ".") -> Path:
    """スキルディレクトリを作成する"""

    # 名前の検証
    if not skill_name.replace("-", "").replace("_", "").isalnum():
        print(f"エラー: スキル名は英数字とハイフンのみ使用可能です: {skill_name}")
        sys.exit(1)

    skill_path = Path(base_path) / skill_name

    if skill_path.exists():
        print(f"エラー: ディレクトリが既に存在します: {skill_path}")
        sys.exit(1)

    # ディレクトリ構造を作成
    directories = [
        skill_path,
        skill_path / "scripts",
        skill_path / "templates",
        skill_path / "references",
    ]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"作成: {directory}")

    # SKILL.md を作成
    skill_md_path = skill_path / "SKILL.md"
    skill_md_path.write_text(SKILL_MD_TEMPLATE.format(name=skill_name), encoding="utf-8")
    print(f"作成: {skill_md_path}")

    # .gitkeep を作成（空ディレクトリ保持用）
    for subdir in ["scripts", "templates", "references"]:
        gitkeep = skill_path / subdir / ".gitkeep"
        gitkeep.touch()

    print(f"\n✅ スキル '{skill_name}' を作成しました: {skill_path}")
    print("\n次のステップ:")
    print(f"  1. {skill_md_path} を編集して description を設定")
    print(f"  2. 必要に応じて scripts/, templates/ にファイルを追加")
    print(f"  3. python quick_validate.py {skill_path} で検証")

    return skill_path


def main():
    parser = argparse.ArgumentParser(
        description="スキルのテンプレートディレクトリを作成"
    )
    parser.add_argument("name", help="スキル名（小文字、ハイフン区切り）")
    parser.add_argument(
        "--path", "-p",
        default=".",
        help="出力先ディレクトリ（デフォルト: カレントディレクトリ）"
    )

    args = parser.parse_args()
    create_skill_directory(args.name, args.path)


if __name__ == "__main__":
    main()
