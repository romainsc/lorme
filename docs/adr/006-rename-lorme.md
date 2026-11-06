# ADR-006: Project rename — lore-mcp → lorme

- **Status:** Accepted
- **Date:** 2026-11-06
- **Supersedes:** ADR-002 (project name selection)
- **Decision:** Rename the project from **lore-mcp** to **lorme**

## Context

ADR-002 selected `lore-mcp` as the project name
in July 2026. At publication time (November 2026),
two blockers emerged:

1. **PyPI collision:** the name `lore-mcp` is
   already registered on PyPI (v1.0.17, ctx-stack,
   Apache 2.0, 15 releases since December 2025).
   Publishing under this name is impossible.

2. **GitHub namespace collision:** 8 repositories
   on GitHub share the exact name `lore-mcp`, two
   with functional overlap (MCP + semantic search).
   Discoverability is compromised.

## Decision

Rename to **lorme** — the fusion of LORE + MCP,
which was the second-ranked candidate in ADR-002.

**LORME = Local Offline Retrieval & MCP Engine**

## Rationale

| Criterion | Score |
|-----------|-------|
| Memorable and distinctive | 5/5 |
| Technically meaningful | 4/5 |
| Short and typeable | 5/5 |
| Pronounceable FR+EN | 5/5 |
| Available (PyPI + GitHub) | 5/5 |

- Preserves the LORE identity that the team knows
- Contains MCP in the portmanteau — no `-mcp`
  suffix needed
- Shortest candidate (5 chars vs 9 for lore-mcp)
- Natural pronunciation in both French and English
- Available on PyPI and GitHub (verified 2026-11-06)

## Alternatives considered

| Name | Why rejected |
|------|-------------|
| lore-mcp | Taken on PyPI (blocker) |
| lorme-mcp | Available but redundant (MCP already in LORME) |
| mnemos-mcp | Available, mythological, but no acronym |
| rune-mcp | Available, good acronym, but gaming connotation |
| arca-mcp | Available, but "arca" unfamiliar in English |

## Consequences

- GitHub repository: `lorme`
- PyPI package: `lorme`
- Python package: `lorme` (under `src/lorme/`)
- CLI entry point: `lorme`
- Class names: `LormeConfig` (was `LoreConfig`)
- The acronym LORME (Local Offline Retrieval &
  MCP Engine) replaces LORE in project identity
- ADR-002 remains as historical record of the
  original naming study

## Provenance

> This document was produced with AI assistance
> (Claude, Anthropic) and reviewed by
> Romain Chantereau.
