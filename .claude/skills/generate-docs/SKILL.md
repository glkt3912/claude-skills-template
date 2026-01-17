---
name: generate-docs
description: ドキュメントを生成する。README、設計書、PR説明文、ADR（Architecture Decision Record）などの作成依頼時に使用。
---

# 目的

プロジェクトの規約に従った各種ドキュメントを生成する。

# 手順

1. **ドキュメント種別の特定**
   - README / PR説明文 / ADR / 設計書 / API仕様書

2. **テンプレートの選択**
   - `templates/` 内から適切なテンプレートを選択

3. **コンテキスト収集**
   - 関連コードや既存ドキュメントを読み込み
   - 変更内容やその理由を把握

4. **ドキュメント生成**
   - テンプレートに沿って内容を記述
   - プロジェクト固有の用語・表現に合わせる

# テンプレート一覧

| ファイル | 用途 |
|----------|------|
| `readme.md.tpl` | プロジェクト README |
| `pr-description.md.tpl` | Pull Request 説明文 |
| `adr.md.tpl` | Architecture Decision Record |

# 制約

- 既存ドキュメントのトーン・スタイルに合わせる
- 技術用語は一貫して使用
- 冗長な説明を避け、簡潔に記述

# 使用例

```
ユーザー: このPRの説明を書いて
実行: 変更内容を分析し、pr-description.md.tpl に沿って説明文を生成
```
