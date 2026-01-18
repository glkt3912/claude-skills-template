---
name: log-analysis
description: ログやスタックトレースを解析する。「ログ解析」「エラーログ見て」「スタックトレース解析」などの依頼時に使用。
---

# 目的

エラーログ、スタックトレース、アプリケーションログを解析し、問題の原因を特定する。

# 手順

1. **ログの種類を特定**
   - エラーログ / アクセスログ / アプリケーションログ

2. **エラー情報の抽出**
   - エラーメッセージ、スタックトレース
   - `references/error-patterns.md` と照合

3. **原因の特定**
   - スタックトレースから発生箇所を特定

# スタックトレースの読み方

```
Error: Cannot read property 'id' of undefined
    at getUserById (/app/src/services/user.ts:45:12)    ← 直接の発生箇所
    at async getProfile (/app/src/handlers/profile.ts:23:18)
    at async Router.handle (/app/node_modules/...)
```

- **1行目**: エラーメッセージ
- **最上部のスタック**: 直接の発生箇所
- **下に行くほど**: 呼び出し元

# 出力フォーマット

```markdown
## ログ解析レポート

### エラー概要
- **種類**: [エラータイプ]
- **メッセージ**: [エラーメッセージ]
- **発生箇所**: `ファイル:行番号`

### 原因分析
[なぜこのエラーが発生したか]

### 推奨対応
1. [対応策]
```

# 参照

- `references/error-patterns.md` - よくあるエラーパターン

# 制約

- 推測ではなくログの事実に基づく
- 機密情報（パスワード、トークン）はマスク
