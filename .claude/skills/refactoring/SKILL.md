---
name: refactoring
description: コードをリファクタリングする。「リファクタ」「コード整理」「可読性向上」「技術的負債解消」などの依頼時に使用。
---

# 目的

外部から見た振る舞いを変えずに、コードの内部構造を改善する。

# 手順

1. **現状分析**
   - コードスメルの特定
   - 改善の優先順位付け

2. **テスト確認**
   - 既存テストの有無を確認
   - 必要なら先にテストを追加

3. **リファクタリング実施**
   - 小さなステップで変更
   - 各ステップ後にテスト実行

4. **検証**
   - 全テストがパスすることを確認
   - パフォーマンスへの影響を確認

# コードスメル一覧

| スメル | 説明 | 対処 |
| ------ | ---- | ---- |
| 長いメソッド | 1つのメソッドが長すぎる | メソッド抽出 |
| 大きなクラス | 責務が多すぎる | クラス分割 |
| 重複コード | 同じコードが複数箇所に | 共通化 |
| 長いパラメータリスト | 引数が多すぎる | オブジェクトにまとめる |
| 変更の分散 | 1つの変更で複数ファイル修正 | 関連コードを集約 |
| ネストが深い | if/for の入れ子が深い | 早期リターン、メソッド抽出 |
| マジックナンバー | 意味不明な数値リテラル | 定数化 |

# リファクタリングパターン

## メソッド抽出

```typescript
// Before
function processOrder(order: Order) {
  // 検証（10行）
  // 計算（15行）
  // 保存（10行）
}

// After
function processOrder(order: Order) {
  validateOrder(order);
  const total = calculateTotal(order);
  saveOrder(order, total);
}
```

## 早期リターン

```typescript
// Before
function getDiscount(user: User) {
  if (user) {
    if (user.isPremium) {
      return 0.2;
    } else {
      return 0.1;
    }
  } else {
    return 0;
  }
}

// After
function getDiscount(user: User) {
  if (!user) return 0;
  if (user.isPremium) return 0.2;
  return 0.1;
}
```

## オブジェクトにまとめる

```typescript
// Before
function createUser(name: string, email: string, age: number, country: string) { ... }

// After
function createUser(params: CreateUserParams) { ... }
```

# 安全なリファクタリングのルール

| ルール | 説明 |
| ------ | ---- |
| テストファースト | リファクタ前にテストを確認/追加 |
| 小さなステップ | 一度に1つの変更 |
| 頻繁にコミット | 動く状態を維持 |
| 振る舞い維持 | 外部仕様は変えない |

# 制約

- 機能追加とリファクタリングは分けて行う
- パフォーマンスクリティカルな箇所は計測してから
- チームのコーディング規約に従う
