# 安全なマイグレーションガイド

## 危険な操作と安全な代替

### カラム削除

```
❌ 危険: いきなり削除
ALTER TABLE users DROP COLUMN old_column;

✅ 安全: 段階的に
1. コードから参照を削除
2. デプロイして確認
3. 後日カラム削除
```

### カラム名変更

```
❌ 危険: いきなり変更
ALTER TABLE users RENAME COLUMN name TO full_name;

✅ 安全: 段階的に
1. 新カラム追加
2. データコピー
3. コード更新
4. 旧カラム削除
```

### NOT NULL 追加

```
❌ 危険: いきなり追加
ALTER TABLE users ADD COLUMN role VARCHAR(50) NOT NULL;

✅ 安全: 段階的に
1. デフォルト値付きで追加
   ALTER TABLE users ADD COLUMN role VARCHAR(50) DEFAULT 'user';
2. 既存データ更新
3. デフォルト削除（必要なら）
```

### 型変更

```
❌ 危険: いきなり変更
ALTER TABLE users ALTER COLUMN age TYPE BIGINT;

✅ 安全: 段階的に
1. 新カラム追加
2. トリガーでデータ同期
3. コード更新
4. 旧カラム削除
```

## ロック時間を最小限に

### 大量データ更新

```sql
-- ❌ 1回で全件更新（長時間ロック）
UPDATE users SET status = 'active';

-- ✅ バッチで分割
UPDATE users SET status = 'active'
WHERE id BETWEEN 1 AND 10000;

UPDATE users SET status = 'active'
WHERE id BETWEEN 10001 AND 20000;
```

### インデックス追加

```sql
-- ❌ 通常のインデックス作成（テーブルロック）
CREATE INDEX idx_users_email ON users(email);

-- ✅ PostgreSQL: CONCURRENTLY オプション
CREATE INDEX CONCURRENTLY idx_users_email ON users(email);
```

## ロールバック計画

すべてのマイグレーションに `down` を用意:

```sql
-- Up
ALTER TABLE users ADD COLUMN role VARCHAR(50) DEFAULT 'user';

-- Down
ALTER TABLE users DROP COLUMN role;
```
