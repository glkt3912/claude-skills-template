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
function createUser(
  name: string,
  email: string,
  age: number,
  country: string
) { ... }

// After
interface CreateUserParams {
  name: string;
  email: string;
  age: number;
  country: string;
}

function createUser(params: CreateUserParams) { ... }
```

## ポリモーフィズムで条件分岐を置換

```typescript
// Before
function calculateArea(shape: Shape) {
  switch (shape.type) {
    case 'circle':
      return Math.PI * shape.radius ** 2;
    case 'rectangle':
      return shape.width * shape.height;
  }
}

// After
interface Shape {
  calculateArea(): number;
}

class Circle implements Shape {
  calculateArea() {
    return Math.PI * this.radius ** 2;
  }
}
```

## Null Object パターン

```typescript
// Before
function getUsername(user: User | null) {
  if (user === null) {
    return 'Guest';
  }
  return user.name;
}

// After
class NullUser implements User {
  name = 'Guest';
}

function getUsername(user: User) {
  return user.name;
}
```
