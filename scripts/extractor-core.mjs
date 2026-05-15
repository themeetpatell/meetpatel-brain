/**
 * Pure logic for mind-graph extraction.
 *
 * No IO here: callers pass in the list of files + their content + git
 * timestamps. This keeps the core trivially testable.
 *
 * Output shape is the source of truth for the public site contract.
 * See docs/superpowers/specs/2026-05-15-living-mind-section-design.md.
 */

import { createHash } from "node:crypto";
import path from "node:path";

// Top-level vault folders → PARA area buckets.
// Anything else (or top-level files) gets bucketed to "inbox".
const AREA_BY_FOLDER = Object.freeze({
  "00 Inbox": "inbox",
  "10 Daily": "daily",
  "20 Compass": "compass",
  "30 Ventures": "ventures",
  "40 Areas": "areas",
  "50 Atlas": "atlas",
  "60 Outputs": "atlas",
  "70 Meta": "meta",
  "99 Archive": "archive",
});

export const VALID_AREAS = Object.freeze([
  "compass",
  "ventures",
  "areas",
  "atlas",
  "meta",
  "daily",
  "inbox",
  "archive",
]);

// 32-char Notion-style UUID, optionally with _all suffix, that may appear at
// the end of an imported filename stem. We strip those before resolving links.
const UUID_TAIL = /[ \-_]+[0-9a-f]{32}(?:_all)?(?=$|\.[^.]+$)/;

// Wikilink: [[Target]] or [[Target|alias]] or [[Target#heading]]
const WIKILINK = /\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]/g;

// Standard markdown link to a local .md target: [text](path.md) or with
// percent-encoded spaces. We ignore http(s)/mailto/anchors and image refs.
const MD_LINK = /(?<!!)\[[^\]]*\]\(([^)]+\.md)(?:#[^)]+)?\)/g;

/**
 * Stable opaque ID for a vault path. 6 hex chars from sha256 → 16M space.
 * Collisions are caught at emit time and widened to 8 chars.
 */
export function hashPath(relPath) {
  return "n_" + createHash("sha256").update(relPath).digest("hex").slice(0, 6);
}

/**
 * Strip Notion UUID suffix from a single filename (stem-only).
 */
export function stripUuid(filename) {
  const ext = path.extname(filename);
  const stem = filename.slice(0, filename.length - ext.length);
  const cleaned = stem.replace(UUID_TAIL, "").trimEnd();
  return cleaned + ext;
}

/**
 * Bucket a vault-relative path into a PARA area.
 */
export function areaFor(relPath) {
  const top = relPath.split(/[\\/]/, 1)[0];
  return AREA_BY_FOLDER[top] ?? "inbox";
}

/**
 * Log-scale a byte size to 1..10.
 */
export function sizeOf(bytes) {
  if (bytes <= 0) return 1;
  const v = Math.round(Math.log2(bytes + 1));
  return Math.max(1, Math.min(10, v - 4));
}

/**
 * Index files by lowercase basename and by lowercase relative-path-without-ext.
 * Used to resolve Obsidian-style shortlinks like [[Biggdate]].
 *
 * If two files share a basename, the basename lookup is dropped for that
 * stem — we never silently pick one.
 */
export function buildLookupIndex(files) {
  const byBasename = new Map();
  const dupedBasenames = new Set();
  const byPath = new Map();
  for (const rel of files) {
    const cleanedRel = rel
      .split(/[\\/]/)
      .map(stripUuid)
      .join("/");
    byPath.set(cleanedRel.toLowerCase().replace(/\.md$/, ""), rel);

    const base = stripUuid(path.basename(rel));
    const stem = base.replace(/\.md$/, "").toLowerCase();
    if (byBasename.has(stem)) dupedBasenames.add(stem);
    else byBasename.set(stem, rel);
  }
  for (const dup of dupedBasenames) byBasename.delete(dup);
  return { byBasename, byPath };
}

/**
 * Resolve a single link target string to a concrete vault-relative path,
 * or null if it doesn't resolve.
 */
export function resolveLink(target, originRel, index) {
  let t;
  try {
    t = decodeURIComponent(target);
  } catch {
    t = target;
  }
  t = t.trim();
  if (!t) return null;
  if (t.startsWith("http://") || t.startsWith("https://")) return null;
  if (t.startsWith("mailto:") || t.startsWith("#") || t.startsWith("data:"))
    return null;

  // 1. Try as a path relative to origin's directory
  const originDir = path.posix.dirname(originRel.replace(/\\/g, "/"));
  const asRel = path.posix
    .normalize(path.posix.join(originDir, t))
    .replace(/^\.\//, "");
  const asRelClean = asRel
    .split("/")
    .map(stripUuid)
    .join("/")
    .toLowerCase()
    .replace(/\.md$/, "");
  if (index.byPath.has(asRelClean)) return index.byPath.get(asRelClean);

  // 2. Absolute-from-vault path
  const asAbs = t
    .split(/[\\/]/)
    .map(stripUuid)
    .join("/")
    .toLowerCase()
    .replace(/\.md$/, "");
  if (index.byPath.has(asAbs)) return index.byPath.get(asAbs);

  // 3. Obsidian shortlink fallback (basename match)
  const stem = stripUuid(path.posix.basename(t))
    .replace(/\.md$/, "")
    .toLowerCase();
  if (index.byBasename.has(stem)) return index.byBasename.get(stem);

  return null;
}

/**
 * Pull link target strings from a markdown body.
 */
export function extractRawLinks(body) {
  const out = [];
  for (const m of body.matchAll(WIKILINK)) out.push(m[1]);
  for (const m of body.matchAll(MD_LINK)) out.push(m[1]);
  return out;
}

/**
 * Build the graph from prepared inputs.
 */
export function buildGraph(inputs) {
  const { files, snapshotMonth, generatedAt, vaultCommit } = inputs;

  const index = buildLookupIndex(files.map((f) => f.relPath));

  const idByPath = new Map();
  const pathById = new Map();
  for (const f of files) {
    let id = hashPath(f.relPath);
    if (pathById.has(id)) {
      id =
        "n_" +
        createHash("sha256").update(f.relPath).digest("hex").slice(0, 8);
    }
    idByPath.set(f.relPath, id);
    pathById.set(id, f.relPath);
  }

  const nodes = files.map((f) => ({
    id: idByPath.get(f.relPath),
    area: areaFor(f.relPath),
    size: sizeOf(f.size),
    createdAt: f.createdAt,
    lastModifiedAt: f.lastModifiedAt,
  }));

  const edgeSet = new Set();
  const edges = [];
  for (const f of files) {
    const sId = idByPath.get(f.relPath);
    const targets = extractRawLinks(f.body);
    for (const raw of targets) {
      const resolved = resolveLink(raw, f.relPath, index);
      if (!resolved) continue;
      const tId = idByPath.get(resolved);
      if (!tId || tId === sId) continue;
      const key = sId < tId ? `${sId}|${tId}` : `${tId}|${sId}`;
      if (edgeSet.has(key)) continue;
      edgeSet.add(key);
      edges.push({ s: sId, t: tId });
    }
  }

  const now = new Date(generatedAt).getTime();
  const dayMs = 86_400_000;
  let addedLast7d = 0;
  let addedLast30d = 0;
  const byArea = Object.fromEntries(VALID_AREAS.map((a) => [a, 0]));
  for (const n of nodes) {
    const age = (now - new Date(n.createdAt).getTime()) / dayMs;
    if (age >= 0 && age <= 7) addedLast7d += 1;
    if (age >= 0 && age <= 30) addedLast30d += 1;
    byArea[n.area] = (byArea[n.area] ?? 0) + 1;
  }

  return {
    snapshot: snapshotMonth,
    generatedAt,
    vaultCommit,
    nodes,
    edges,
    stats: {
      noteCount: nodes.length,
      edgeCount: edges.length,
      addedLast7d,
      addedLast30d,
      byArea,
    },
  };
}

/**
 * Fail loud if a forbidden field appears in the serialized graph.
 */
export function assertPrivacyInvariants(graph) {
  const json = JSON.stringify(graph);
  const forbidden = [
    "\"title\":",
    "\"body\":",
    "\"tags\":",
    "\"alias\":",
    "\"aliases\":",
    "\"frontmatter\":",
    "\"path\":",
    "\"filename\":",
  ];
  for (const k of forbidden) {
    if (json.includes(k)) {
      throw new Error(`privacy: forbidden key '${k}' present in graph output`);
    }
  }
  for (const n of graph.nodes) {
    if (!n.id.startsWith("n_") || n.id.length > 10) {
      throw new Error(`privacy: node id '${n.id}' does not match opaque shape`);
    }
    if (!VALID_AREAS.includes(n.area)) {
      throw new Error(`privacy: node area '${n.area}' not in allowlist`);
    }
  }
}
