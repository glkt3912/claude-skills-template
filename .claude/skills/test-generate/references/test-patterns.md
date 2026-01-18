# テストパターン集

## AAA パターン

```typescript
describe('calculateTotal', () => {
  it('should calculate total with tax', () => {
    // Arrange: 準備
    const items = [{ price: 100 }, { price: 200 }];
    const taxRate = 0.1;

    // Act: 実行
    const result = calculateTotal(items, taxRate);

    // Assert: 検証
    expect(result).toBe(330);
  });
});
```

## テストケースの観点

| 観点 | 例 |
| ---- | -- |
| 正常系 | 期待通りの入力で期待通りの出力 |
| 異常系 | 不正な入力でエラーハンドリング |
| 境界値 | 最小値、最大値、0、空文字、null |
| エッジケース | 配列が空、1要素、大量要素 |

## モック戦略

| 依存の種類 | 方針 |
| ---------- | ---- |
| 外部 API | 必ずモック |
| データベース | 単体テストではモック |
| ファイルシステム | 単体テストではモック |
| 時刻 | 固定値に差し替え |
| 乱数 | シード固定またはモック |

## モックの例

```typescript
// 外部APIのモック
vi.mock('./api', () => ({
  fetchUser: vi.fn().mockResolvedValue({ id: 1, name: 'Test' })
}));

// 時刻のモック
vi.useFakeTimers();
vi.setSystemTime(new Date('2024-01-01'));

// 関数のスパイ
const spy = vi.spyOn(console, 'log');
expect(spy).toHaveBeenCalledWith('message');
```

## パラメータ化テスト

```typescript
describe.each([
  { input: 0, expected: 'zero' },
  { input: 1, expected: 'one' },
  { input: 2, expected: 'two' },
])('numberToWord($input)', ({ input, expected }) => {
  it(`returns ${expected}`, () => {
    expect(numberToWord(input)).toBe(expected);
  });
});
```

## 非同期テスト

```typescript
// async/await
it('fetches user', async () => {
  const user = await fetchUser(1);
  expect(user.name).toBe('Test');
});

// Promise
it('fetches user', () => {
  return fetchUser(1).then(user => {
    expect(user.name).toBe('Test');
  });
});
```
