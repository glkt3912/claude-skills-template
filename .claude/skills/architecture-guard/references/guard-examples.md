# ガードレール実装例

## 1. OpenAPI 仕様との整合性チェック

```typescript
/**
 * @what 全ての registerRoute 呼び出しが OpenAPI 定義と一致すること
 * @why API 仕様と実装の乖離を防ぐため
 * @failure 未定義のエンドポイントや型の不一致が本番に流出する
 */
export async function checkOpenApiConsistency() {
  const routes = await extractRoutes('src/routes/**/*.ts');
  const spec = await loadOpenApiSpec('openapi.yaml');

  const violations = routes.filter(route =>
    !spec.paths[route.path]?.[route.method]
  );

  if (violations.length > 0) {
    console.error('OpenAPI 未定義のルート:', violations);
    process.exit(1);
  }
}
```

## 2. Result<T> 型の強制

```typescript
/**
 * @what リポジトリメソッドの戻り値が Promise<Result<T, E>> であること
 * @why エラー分類の一貫性を保証するため
 * @failure 生の Promise だと例外処理が不統一になる
 */
export async function checkResultType() {
  const repoFiles = await glob('src/repositories/**/*.ts');

  for (const file of repoFiles) {
    const methods = await extractMethodSignatures(file);
    const violations = methods.filter(m =>
      m.returnType.startsWith('Promise<') &&
      !m.returnType.includes('Result<')
    );

    if (violations.length > 0) {
      console.error(`${file}: Result<T> を使用していないメソッド:`, violations);
      process.exit(1);
    }
  }
}
```

## 3. 依存方向の検証

```typescript
/**
 * @what domain 層が infrastructure 層に依存していないこと
 * @why クリーンアーキテクチャの依存ルールを守るため
 * @failure ビジネスロジックが外部実装に結合し、テスト困難になる
 */
export async function checkDependencyDirection() {
  const domainFiles = await glob('src/domain/**/*.ts');

  for (const file of domainFiles) {
    const imports = await extractImports(file);
    const violations = imports.filter(i =>
      i.includes('/infrastructure/') ||
      i.includes('/adapters/')
    );

    if (violations.length > 0) {
      console.error(`${file}: 禁止された依存:`, violations);
      process.exit(1);
    }
  }
}
```

## 4. ドメインイベント構造検査

```typescript
/**
 * @what イベントクラスに必須フィールドが存在すること
 * @why イベント追跡・デバッグを可能にするため
 * @failure イベント系列の追跡が不可能になる
 */
const REQUIRED_FIELDS = ['causationId', 'correlationId', 'emittedAt'];

export async function checkDomainEvents() {
  const eventFiles = await glob('src/domain/events/**/*.ts');

  for (const file of eventFiles) {
    const classes = await extractClasses(file);
    for (const cls of classes) {
      const missing = REQUIRED_FIELDS.filter(f =>
        !cls.properties.includes(f)
      );

      if (missing.length > 0) {
        console.error(`${file}/${cls.name}: 必須フィールド不足:`, missing);
        process.exit(1);
      }
    }
  }
}
```

## 5. 命名規則の検証

```typescript
/**
 * @what ファイル名とエクスポートされるクラス名が一致すること
 * @why コードベースの予測可能性を高めるため
 * @failure ファイルを探す際の認知負荷が増大する
 */
export async function checkNamingConsistency() {
  const files = await glob('src/**/*.ts');

  for (const file of files) {
    const fileName = path.basename(file, '.ts');
    const exports = await extractExports(file);
    const mainExport = exports.find(e => e.isDefault || e.name === toPascalCase(fileName));

    if (!mainExport) {
      console.error(`${file}: ファイル名と一致するエクスポートがない`);
      process.exit(1);
    }
  }
}
```

## ESLint との使い分け

| ESLint で対応 | カスタムガードレールで対応 |
| ------------- | -------------------------- |
| import 制約（単一ファイル） | 複数ファイル横断の整合性 |
| 禁止パターン | 型情報を使った検証 |
| フォーマット | 外部ファイル（OpenAPI等）との照合 |
