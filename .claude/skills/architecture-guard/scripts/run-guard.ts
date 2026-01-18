#!/usr/bin/env npx ts-node
/**
 * ガードレール統一実行ラッパー
 *
 * @what 全ガードレールを標準化された形式で実行する
 * @why 実行結果の集計・分析を可能にするため
 * @failure 個別実行だと履歴追跡やレポート生成が困難
 *
 * 使用方法:
 *   npx ts-node run-guard.ts <guard-name>
 *   npx ts-node run-guard.ts --all
 */

import * as fs from 'fs';
import * as path from 'path';

interface GuardResult {
  name: string;
  status: 'pass' | 'fail';
  violations: string[];
  timestamp: string;
  duration: number;
}

interface Guard {
  name: string;
  what: string;
  why: string;
  failure: string;
  run: () => Promise<string[]>;
}

// ガードレール定義（実際のプロジェクトでは別ファイルからインポート）
const guards: Guard[] = [
  // 例: 依存方向チェック
  // {
  //   name: 'dependency-direction',
  //   what: 'domain 層が infrastructure 層に依存していないこと',
  //   why: 'クリーンアーキテクチャの依存ルールを守るため',
  //   failure: 'ビジネスロジックが外部実装に結合する',
  //   run: async () => { /* 実装 */ return []; }
  // }
];

async function runGuard(guard: Guard): Promise<GuardResult> {
  const start = Date.now();

  try {
    const violations = await guard.run();
    const duration = Date.now() - start;

    return {
      name: guard.name,
      status: violations.length === 0 ? 'pass' : 'fail',
      violations,
      timestamp: new Date().toISOString(),
      duration,
    };
  } catch (error) {
    return {
      name: guard.name,
      status: 'fail',
      violations: [String(error)],
      timestamp: new Date().toISOString(),
      duration: Date.now() - start,
    };
  }
}

async function runAllGuards(): Promise<GuardResult[]> {
  const results: GuardResult[] = [];

  for (const guard of guards) {
    console.log(`Running: ${guard.name}`);
    console.log(`  @what: ${guard.what}`);

    const result = await runGuard(guard);
    results.push(result);

    if (result.status === 'pass') {
      console.log(`  ✅ PASS (${result.duration}ms)`);
    } else {
      console.log(`  ❌ FAIL (${result.duration}ms)`);
      console.log(`  @why: ${guard.why}`);
      console.log(`  @failure: ${guard.failure}`);
      result.violations.forEach(v => console.log(`    - ${v}`));
    }
    console.log();
  }

  return results;
}

function writeResults(results: GuardResult[], outputPath: string) {
  // NDJSON 形式で履歴に追記
  const ndjson = results.map(r => JSON.stringify(r)).join('\n') + '\n';
  fs.appendFileSync(outputPath, ndjson);
}

async function main() {
  const args = process.argv.slice(2);
  const outputPath = process.env.GUARD_OUTPUT || 'guard-results.ndjson';

  let results: GuardResult[];

  if (args.includes('--all') || args.length === 0) {
    results = await runAllGuards();
  } else {
    const guardName = args[0];
    const guard = guards.find(g => g.name === guardName);

    if (!guard) {
      console.error(`Unknown guard: ${guardName}`);
      console.error(`Available guards: ${guards.map(g => g.name).join(', ')}`);
      process.exit(1);
    }

    results = [await runGuard(guard)];
  }

  // 結果を履歴に記録
  writeResults(results, outputPath);

  // サマリー
  const passed = results.filter(r => r.status === 'pass').length;
  const failed = results.filter(r => r.status === 'fail').length;

  console.log('='.repeat(50));
  console.log(`Results: ${passed} passed, ${failed} failed`);

  // 1つでも失敗があれば非ゼロ終了
  if (failed > 0) {
    process.exit(1);
  }
}

main().catch(console.error);
