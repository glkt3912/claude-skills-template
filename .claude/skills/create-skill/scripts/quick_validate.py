#!/usr/bin/env python3
"""
SKILL.md の構文・構造を検証するスクリプト

使用方法:
    python quick_validate.py <skill-path>

例:
    python quick_validate.py .claude/skills/my-skill
    python quick_validate.py .claude/skills/my-skill/SKILL.md
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List, Tuple


class ValidationError:
    def __init__(self, level: str, message: str):
        self.level = level  # "error" or "warning"
        self.message = message

    def __str__(self):
        icon = "❌" if self.level == "error" else "⚠️"
        return f"{icon} [{self.level.upper()}] {self.message}"


def validate_skill(skill_path: Path) -> List[ValidationError]:
    """スキルを検証し、エラーリストを返す"""
    errors: List[ValidationError] = []

    # パスの正規化
    if skill_path.name == "SKILL.md":
        skill_dir = skill_path.parent
        skill_md = skill_path
    else:
        skill_dir = skill_path
        skill_md = skill_path / "SKILL.md"

    # SKILL.md の存在確認
    if not skill_md.exists():
        errors.append(ValidationError("error", f"SKILL.md が見つかりません: {skill_md}"))
        return errors

    content = skill_md.read_text(encoding="utf-8")

    # Frontmatter の検証
    frontmatter_errors = validate_frontmatter(content)
    errors.extend(frontmatter_errors)

    # 本文の検証
    body_errors = validate_body(content)
    errors.extend(body_errors)

    # ディレクトリ構造の検証
    structure_errors = validate_structure(skill_dir)
    errors.extend(structure_errors)

    return errors


def validate_frontmatter(content: str) -> List[ValidationError]:
    """Frontmatter を検証"""
    errors: List[ValidationError] = []

    # Frontmatter の存在確認
    if not content.startswith("---"):
        errors.append(ValidationError("error", "Frontmatter が見つかりません（--- で開始してください）"))
        return errors

    # Frontmatter の終了確認
    parts = content.split("---", 2)
    if len(parts) < 3:
        errors.append(ValidationError("error", "Frontmatter が閉じられていません（--- で終了してください）"))
        return errors

    frontmatter = parts[1].strip()

    # name フィールドの検証
    name_match = re.search(r'^name:\s*(.+)$', frontmatter, re.MULTILINE)
    if not name_match:
        errors.append(ValidationError("error", "必須フィールド 'name' がありません"))
    else:
        name = name_match.group(1).strip().strip('"').strip("'")
        if len(name) > 64:
            errors.append(ValidationError("error", f"name は64文字以下にしてください（現在: {len(name)}文字）"))
        if not re.match(r'^[a-z0-9-]+$', name):
            errors.append(ValidationError("error", "name は小文字、数字、ハイフンのみ使用可能です"))

    # description フィールドの検証
    desc_match = re.search(r'^description:\s*(.+?)(?=^[a-z-]+:|\Z)', frontmatter, re.MULTILINE | re.DOTALL)
    if not desc_match:
        errors.append(ValidationError("error", "必須フィールド 'description' がありません"))
    else:
        desc = desc_match.group(1).strip()
        # 複数行の場合は | や > を除去
        desc = re.sub(r'^[|>]\s*', '', desc)
        desc_text = ' '.join(desc.split())

        if len(desc_text) < 10:
            errors.append(ValidationError("warning", "description が短すぎます（具体的なトリガーワードを含めてください）"))
        if len(desc_text) > 1024:
            errors.append(ValidationError("error", f"description は1024文字以下にしてください（現在: {len(desc_text)}文字）"))

    # version/author がトップレベルにないか確認
    if re.search(r'^version:\s*', frontmatter, re.MULTILINE):
        if not re.search(r'^metadata:', frontmatter, re.MULTILINE):
            errors.append(ValidationError("warning", "version は metadata セクション下に配置することを推奨します"))

    if re.search(r'^author:\s*', frontmatter, re.MULTILINE):
        if not re.search(r'^metadata:', frontmatter, re.MULTILINE):
            errors.append(ValidationError("warning", "author は metadata セクション下に配置することを推奨します"))

    return errors


def validate_body(content: str) -> List[ValidationError]:
    """本文を検証"""
    errors: List[ValidationError] = []

    parts = content.split("---", 2)
    if len(parts) < 3:
        return errors

    body = parts[2].strip()
    lines = body.split("\n")

    # 行数チェック
    if len(lines) > 500:
        errors.append(ValidationError("warning", f"SKILL.md が長すぎます（{len(lines)}行）。500行以下を推奨します"))

    # 見出しの存在確認
    if not re.search(r'^#\s+', body, re.MULTILINE):
        errors.append(ValidationError("warning", "見出し（#）がありません"))

    return errors


def validate_structure(skill_dir: Path) -> List[ValidationError]:
    """ディレクトリ構造を検証"""
    errors: List[ValidationError] = []

    if not skill_dir.is_dir():
        return errors

    # scripts/ 内のファイル検証
    scripts_dir = skill_dir / "scripts"
    if scripts_dir.exists():
        for script in scripts_dir.glob("*.py"):
            content = script.read_text(encoding="utf-8")
            # 危険なパターンのチェック（簡易）
            if "os.system" in content or "subprocess.call" in content:
                if "shell=True" in content:
                    errors.append(ValidationError("warning", f"shell=True の使用を検出: {script.name}"))

    return errors


def main():
    parser = argparse.ArgumentParser(
        description="SKILL.md の構文・構造を検証"
    )
    parser.add_argument("path", help="スキルディレクトリまたは SKILL.md のパス")

    args = parser.parse_args()
    skill_path = Path(args.path)

    if not skill_path.exists():
        print(f"❌ パスが見つかりません: {skill_path}")
        sys.exit(1)

    print(f"検証中: {skill_path}\n")

    errors = validate_skill(skill_path)

    if not errors:
        print("✅ 検証完了: 問題は見つかりませんでした")
        sys.exit(0)

    error_count = sum(1 for e in errors if e.level == "error")
    warning_count = sum(1 for e in errors if e.level == "warning")

    for error in errors:
        print(error)

    print(f"\n結果: {error_count} エラー, {warning_count} 警告")

    if error_count > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
