# Claude Code Skills 完全ガイド

## Skills とは

**Skills（スキル）** は、Claude Code に専門的な能力を追加する「知識パッケージ」です。

指示・スクリプト・リソースをまとめたフォルダで、特定タスクを効率的に実行するための仕組みです。

```
通常の Claude    → 汎用的な応答
Skills 適用時   → タスク特化の応答（手順・制約・ツール付き）
```

---

## 核となる設計原則: Progressive Disclosure

**段階的開示** - 必要な情報を、必要なときに、必要な分だけ読み込む

コンテキストウィンドウは有限リソースです。すべてを最初から読み込むとトークンを浪費します。

### 3つの段階

| レベル | タイミング | 読み込む内容 |
| ------ | ---------- | ------------ |
| 1 | 起動時 | `name` と `description` のみ |
| 2 | Skill 発火時 | SKILL.md の本文 |
| 3 | 実行時 | scripts / references / assets（必要に応じて） |

---

## ディレクトリ構成

```
my-skill/
├── SKILL.md              # 必須：メタデータと指示
├── scripts/              # 任意：実行可能コード
│   └── helper.py
├── references/           # 任意：参照ドキュメント
│   └── api-spec.md
├── templates/            # 任意：テンプレートファイル
│   └── component.tsx.tpl
└── assets/               # 任意：その他リソース
    └── icon.png
```

### 各ディレクトリの役割

| ディレクトリ | 用途 | 例 |
| ------------ | ---- | -- |
| `scripts/` | 実行可能なツール | Python, Bash スクリプト |
| `references/` | 参照情報 | API 仕様、DB スキーマ |
| `templates/` | 生成用テンプレート | コード、ドキュメントの雛形 |
| `assets/` | その他リソース | 画像、フォント |

---

## 配置場所

| 場所 | スコープ | 用途 |
| ---- | -------- | ---- |
| `~/.claude/skills/` | 個人・全プロジェクト共通 | 個人用スキル |
| `.claude/skills/` | プロジェクト固有 | チーム共有スキル |

---

## SKILL.md の書き方

### 基本構造

```markdown
---
name: my-skill-name
description: このスキルの説明。いつ使うべきかを含める。
---

# スキル名

## 目的
[このスキルが何を達成するか]

## 手順
1. [ステップ1]
2. [ステップ2]

## 制約
- [制約1]
- [制約2]

## 使用例
[具体的な使用例]
```

### Frontmatter フィールド

#### 必須

| フィールド | 制限 | 説明 |
| ---------- | ---- | ---- |
| `name` | 64文字、小文字・数字・ハイフンのみ | スキルの識別子 |
| `description` | 1024文字 | **呼び出し判断の基準**（最重要） |

#### オプション

```yaml
---
name: my-skill
description: 説明文
allowed-tools:
  - Bash
  - Read
  - Write
metadata:
  author: your-name
  version: "1.0.0"
---
```

> **注意**: `version` や `author` をトップレベルに書くとエラー。必ず `metadata` 下に配置。

---

## description の書き方（最重要）

**Claude は `description` を見て「このスキルを使うべきか」を判断します。**

### 悪い例

```yaml
description: PDF処理
```

→ 曖昧すぎて発火しない

### 良い例

```yaml
description: |
  PDFからテキスト・表を抽出する。
  「PDF解析」「PDFからテキスト抽出」などの依頼時に使用。
```

→ 具体的なキーワードとトリガー条件を含む

### 推奨フォーマット

```yaml
description: [何をするか]。「[トリガーワード1]」「[トリガーワード2]」などの依頼時に使用。
```

---

## スキルの呼び出し方法

### 1. 自動呼び出し（推奨）

Claude が `description` を読み、タスクに合致すれば自動で選択・適用。

```
ユーザー: このコードをレビューして
Claude: (code-review スキルを自動選択)
```

### 2. 明示的呼び出し

スラッシュコマンドで直接指定。

```
/code-review
/commit
```

---

## ベストプラクティス

### 1. 簡潔に保つ

- SKILL.md は **500行以下** を目安
- Claude が既知の情報は省略
- 詳細は `references/` に分離

### 2. 命令形で記述

```markdown
❌ You should first check the file format.
✅ First, verify the file format using validate.py.
```

### 3. 具体例を含める

抽象的な説明より、具体的な入出力例が効果的。

### 4. 段階的に改善

1. 実タスクでスキルを使用
2. 問題点を特定
3. SKILL.md を更新
4. 再テスト

---

## スクリプトの活用

### 実行 vs 参照

| 用途 | 方法 | コンテキスト消費 |
| ---- | ---- | ---------------- |
| 実行 | `python scripts/helper.py` | 出力のみ（少ない） |
| 参照 | ファイル内容を読み込み | 全文（多い） |

厳密な処理（フォーマット、計算）はスクリプトに任せ、出力だけを使うのが効率的。

---

## セキュリティ

### チェックリスト

- [ ] API キーやパスワードをハードコードしていない
- [ ] 外部ネットワークへの意図しない接続がない
- [ ] ファイルアクセスの範囲が適切

### 注意

> 信頼できるソース（自作または公式）のスキルのみを使用してください。
> 第三者のスキルは必ずコードを監査してから使用。

---

## スキル作成の判断基準

### 適している場面

- 繰り返し発生するタスク
- 手順が明確なワークフロー
- プロジェクト固有のパターンがある

### 適さない場面

- 一度きりのタスク
- 頻繁に変わる要件
- 外部 API 連携が主体（MCP サーバーの方が適切）

---

## 参考リンク

- [Agent Skills - Claude Code Docs](https://code.claude.com/docs/en/skills)
- [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [GitHub - anthropics/skills](https://github.com/anthropics/skills)
