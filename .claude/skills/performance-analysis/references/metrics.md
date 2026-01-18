# パフォーマンス指標一覧

## フロントエンド（Core Web Vitals）

| 指標 | 目標 | 説明 |
| ---- | ---- | ---- |
| LCP | < 2.5s | Largest Contentful Paint（最大コンテンツの描画） |
| FID | < 100ms | First Input Delay（初回入力遅延） |
| CLS | < 0.1 | Cumulative Layout Shift（累積レイアウトシフト） |
| TTFB | < 800ms | Time to First Byte（最初のバイト到達時間） |
| FCP | < 1.8s | First Contentful Paint（最初のコンテンツ描画） |
| TTI | < 3.8s | Time to Interactive（操作可能になるまでの時間） |

## バックエンド

| 指標 | 目標 | 説明 |
| ---- | ---- | ---- |
| Response Time (p50) | < 100ms | 中央値の応答時間 |
| Response Time (p95) | < 200ms | 95パーセンタイルの応答時間 |
| Response Time (p99) | < 500ms | 99パーセンタイルの応答時間 |
| Throughput | 高いほど良い | 秒間リクエスト数 (RPS) |
| Error Rate | < 1% | エラー率 |
| CPU Usage | < 70% | CPU 使用率 |
| Memory Usage | 安定 | メモリ使用量（リークなし） |

## データベース

| 指標 | 目標 | 説明 |
| ---- | ---- | ---- |
| Query Time (p95) | < 100ms | クエリ実行時間 |
| Slow Query Count | 0 | スロークエリの数 |
| Connection Pool Usage | < 80% | コネクションプール使用率 |
| Index Hit Rate | > 99% | インデックス使用率 |
| Lock Wait Time | 最小 | ロック待ち時間 |
