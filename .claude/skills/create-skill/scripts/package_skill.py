#!/usr/bin/env python3
"""
スキルを .skill ファイル（ZIP形式）にパッケージするスクリプト

使用方法:
    python package_skill.py <skill-path> [--output <output-path>]

例:
    python package_skill.py .claude/skills/my-skill
    python package_skill.py .claude/skills/my-skill --output ./dist
"""

import argparse
import os
import re
import sys
import zipfile
from pathlib import Path
from datetime import datetime


def get_skill_name(skill_path: Path) -> str:
    """SKILL.md から name を取得"""
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return skill_path.name

    content = skill_md.read_text(encoding="utf-8")
    match = re.search(r'^name:\s*(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip().strip('"').strip("'")
    return skill_path.name


def package_skill(skill_path: Path, output_dir: Path = None) -> Path:
    """スキルをパッケージ化"""

    if not skill_path.is_dir():
        print(f"❌ ディレクトリが見つかりません: {skill_path}")
        sys.exit(1)

    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        print(f"❌ SKILL.md が見つかりません: {skill_md}")
        sys.exit(1)

    # 出力先の決定
    if output_dir is None:
        output_dir = Path(".")
    output_dir.mkdir(parents=True, exist_ok=True)

    # ファイル名の生成
    skill_name = get_skill_name(skill_path)
    timestamp = datetime.now().strftime("%Y%m%d")
    output_file = output_dir / f"{skill_name}-{timestamp}.skill"

    # 除外パターン
    exclude_patterns = [
        "__pycache__",
        ".pyc",
        ".git",
        ".DS_Store",
        ".gitkeep",
    ]

    def should_exclude(path: Path) -> bool:
        for pattern in exclude_patterns:
            if pattern in str(path):
                return True
        return False

    # ZIP ファイルの作成
    with zipfile.ZipFile(output_file, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in skill_path.rglob("*"):
            if file_path.is_file() and not should_exclude(file_path):
                arcname = file_path.relative_to(skill_path)
                zf.write(file_path, arcname)
                print(f"  追加: {arcname}")

    print(f"\n✅ パッケージ作成完了: {output_file}")
    print(f"   サイズ: {output_file.stat().st_size:,} bytes")

    return output_file


def main():
    parser = argparse.ArgumentParser(
        description="スキルを .skill ファイルにパッケージ"
    )
    parser.add_argument("path", help="スキルディレクトリのパス")
    parser.add_argument(
        "--output", "-o",
        default=None,
        help="出力先ディレクトリ（デフォルト: カレントディレクトリ）"
    )

    args = parser.parse_args()
    skill_path = Path(args.path)
    output_dir = Path(args.output) if args.output else None

    package_skill(skill_path, output_dir)


if __name__ == "__main__":
    main()
