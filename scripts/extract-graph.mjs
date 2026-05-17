#!/usr/bin/env node
/**
 * CLI driver: walks the vault, runs the extractor, writes graph snapshots
 * to public/mind/. Invoked locally and by the nightly Action.
 *
 * Usage:
 *   node scripts/extract-graph.mjs --vault <path> --out <path>
 *
 * Defaults: --vault . --out public/mind
 */

import { readFile, writeFile, mkdir, readdir, stat } from "node:fs/promises";
import { execFile } from "node:child_process";
import path from "node:path";
import { promisify } from "node:util";
import {
  buildGraph,
  assertPrivacyInvariants,
} from "./extractor-core.mjs";

const execFileP = promisify(execFile);

const EXCLUDED_DIRS = new Set([
  ".git",
  ".obsidian",
  ".claude",
  "node_modules",
  "dist",
  ".vscode",
  ".idea",
]);

const EXCLUDED_PREFIXES = ["docs/superpowers/"];

function parseArgs(argv) {
  const args = { vault: ".", out: "public/mind" };
  for (let i = 2; i < argv.length; i += 1) {
    const a = argv[i];
    if (a === "--vault") args.vault = argv[++i];
    else if (a === "--out") args.out = argv[++i];
  }
  return args;
}

async function* walkMd(root, rel = "") {
  const here = rel ? path.join(root, rel) : root;
  let entries;
  try {
    entries = await readdir(here, { withFileTypes: true });
  } catch {
    return;
  }
  for (const e of entries) {
    if (e.name.startsWith(".")) continue;
    const childRel = rel ? path.posix.join(rel, e.name) : e.name;
    if (e.isDirectory()) {
      if (EXCLUDED_DIRS.has(e.name)) continue;
      yield* walkMd(root, childRel);
    } else if (e.isFile() && e.name.endsWith(".md")) {
      if (EXCLUDED_PREFIXES.some((p) => childRel.startsWith(p))) continue;
      yield childRel;
    }
  }
}

async function gitTimestamps(vault, relPath) {
  let lastModifiedAt = "";
  try {
    const { stdout } = await execFileP(
      "git",
      ["log", "-1", "--format=%cI", "--", relPath],
      { cwd: vault, maxBuffer: 4 * 1024 * 1024 },
    );
    lastModifiedAt = stdout.trim().slice(0, 10);
  } catch {
    /* leave empty */
  }
  let createdAt = "";
  try {
    const { stdout } = await execFileP(
      "git",
      [
        "log",
        "--diff-filter=A",
        "--reverse",
        "--format=%cI",
        "--",
        relPath,
      ],
      { cwd: vault, maxBuffer: 4 * 1024 * 1024 },
    );
    const first = stdout.trim().split("\n")[0];
    createdAt = first ? first.slice(0, 10) : lastModifiedAt;
  } catch {
    createdAt = lastModifiedAt;
  }
  return { createdAt, lastModifiedAt };
}

async function gitHead(vault) {
  try {
    const { stdout } = await execFileP(
      "git",
      ["rev-parse", "--short", "HEAD"],
      { cwd: vault },
    );
    return stdout.trim();
  } catch {
    return "unknown";
  }
}

async function main() {
  const { vault, out } = parseArgs(process.argv);
  const absVault = path.resolve(vault);
  const absOut = path.resolve(out);

  process.stderr.write(`Extracting from ${absVault}\n`);

  const relPaths = [];
  for await (const rel of walkMd(absVault)) relPaths.push(rel);
  process.stderr.write(`Found ${relPaths.length} markdown files\n`);

  const files = [];
  let i = 0;
  for (const relPath of relPaths) {
    i += 1;
    if (i % 200 === 0) process.stderr.write(`  ...processed ${i}\n`);
    const abs = path.join(absVault, relPath);
    let stats;
    try {
      stats = await stat(abs);
    } catch {
      continue;
    }
    let body = "";
    try {
      body = await readFile(abs, "utf8");
    } catch {
      continue;
    }
    const ts = await gitTimestamps(absVault, relPath);
    const today = new Date().toISOString().slice(0, 10);
    files.push({
      relPath,
      size: stats.size,
      body,
      createdAt: ts.createdAt || today,
      lastModifiedAt: ts.lastModifiedAt || today,
    });
  }

  const generatedAt = new Date().toISOString();
  const snapshotMonth = generatedAt.slice(0, 7);
  const vaultCommit = await gitHead(absVault);
  const graph = buildGraph({
    files,
    snapshotMonth,
    generatedAt,
    vaultCommit,
  });

  assertPrivacyInvariants(graph);

  await mkdir(absOut, { recursive: true });
  const latestPath = path.join(absOut, "graph.latest.json");
  const monthPath = path.join(absOut, `graph.${snapshotMonth}.json`);
  await writeFile(latestPath, JSON.stringify(graph) + "\n", "utf8");
  await writeFile(monthPath, JSON.stringify(graph) + "\n", "utf8");

  const indexPath = path.join(absOut, "index.json");
  let manifest = { latest: "graph.latest.json", snapshots: [] };
  try {
    manifest = JSON.parse(await readFile(indexPath, "utf8"));
  } catch {
    /* fresh */
  }
  const otherSnapshots = (manifest.snapshots ?? []).filter(
    (s) => s.month !== snapshotMonth,
  );
  manifest.latest = "graph.latest.json";
  manifest.snapshots = [
    {
      month: snapshotMonth,
      file: `graph.${snapshotMonth}.json`,
      vaultCommit,
      noteCount: graph.stats.noteCount,
    },
    ...otherSnapshots,
  ].sort((a, b) => b.month.localeCompare(a.month));
  await writeFile(indexPath, JSON.stringify(manifest, null, 2) + "\n", "utf8");

  process.stderr.write(
    `Wrote ${latestPath}\n` +
      `Wrote ${monthPath}\n` +
      `Wrote ${indexPath}\n` +
      `Nodes: ${graph.stats.noteCount}, edges: ${graph.stats.edgeCount}, ` +
      `+${graph.stats.addedLast7d} (7d), +${graph.stats.addedLast30d} (30d)\n`,
  );
}

main().catch((err) => {
  process.stderr.write(`extract failed: ${err.message}\n`);
  process.exit(1);
});
