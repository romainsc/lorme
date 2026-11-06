# Grooming E0.10 — Project rename study

## Context

`lore-mcp` is already taken on PyPI (v1.0.17,
ctx-stack, Apache 2.0, 15 releases since Dec
2025). The name cannot be used for PyPI
publication. Additionally, 8 GitHub repos share
the exact name `lore-mcp`, two with functional
overlap (MCP + semantic search).

This is a **hard blocker** for E4.02 (PyPI
publish) — not a preference, a constraint.

## Scope

Study + execute the rename of the project.
Evaluate candidates, select one, apply the
rename across all artifacts.

## Candidates

Sourced from ADR-002 shortlist + new candidates.
All verified available on PyPI and GitHub
(2026-11-06).

### Tier 1: strong candidates

| Name | Acronym | PyPI | GitHub | Pros | Cons |
|------|---------|------|--------|------|------|
| **lorme** | LORE + MCP fusion | Free | Free | Distinctive, short, pronounceable FR+EN, preserves LORE identity. ADR-002 second choice. CLI: `lorme`. Import: `lorme` | No explicit MCP suffix — but LORME *contains* MCP |
| **lorme-mcp** | LORME + explicit MCP | Free | Free | Maximum clarity: identity + protocol | Redundant (MCP is already in LORME). Longer to type |
| **mnemos-mcp** | Mnemosyne (memory) | Free | TBV | Mythological resonance, memorable, pronounceable | No acronym, less technically descriptive |

### Tier 2: acceptable

| Name | Acronym | PyPI | GitHub | Pros | Cons |
|------|---------|------|--------|------|------|
| **rune-mcp** | Retrieval Using Neural Embeddings | Free | TBV | Good acronym, symbolic | "rune" evokes gaming/fantasy more than knowledge |
| **arca-mcp** | ARCA Retrieves Chunks Autonomously | Free | TBV | Recursive acronym, Latin roots | Less intuitive, "arca" unknown in English |

### Eliminated

| Name | Reason |
|------|--------|
| lore-mcp | Taken on PyPI (blocker) |
| lore | Taken on PyPI (ML framework) |
| lore-ai | Taken on PyPI |
| cairn-mcp | Taken on PyPI |

## Evaluation criteria (from ADR-002)

1. **Memorable and distinctive** — stands out in
   the MCP ecosystem
2. **Technically meaningful** — conveys what the
   tool does
3. **Short and typeable** — works as CLI, PyPI,
   GitHub
4. **Pronounceable** — in both English and French
5. **Available** — PyPI + GitHub (hard constraint)

## Scoring

| Criterion | lorme | lorme-mcp | mnemos-mcp | rune-mcp | arca-mcp |
|-----------|-------|-----------|------------|----------|----------|
| Memorable | 5 | 4 | 5 | 4 | 3 |
| Technically meaningful | 4 | 5 | 3 | 5 | 4 |
| Short and typeable | 5 | 3 | 3 | 3 | 3 |
| Pronounceable FR+EN | 5 | 4 | 4 | 4 | 3 |
| Available | 5 | 5 | 5 | 5 | 5 |
| **Total** | **24** | **21** | **20** | **21** | **18** |

## Recommendation

**lorme** — best overall score, shortest,
preserves the LORE identity that the team knows,
contains MCP in the portmanteau. The `-mcp`
suffix is unnecessary because LORME *is*
LORE+MCP.

Expansion: **LORME = Local Offline Retrieval
& MCP Engine** (or simply the fusion of
LORE + MCP, no forced expansion needed).

## Rename impact (DoD)

If a rename is decided, the following artifacts
must be updated:

### MVP1: Code rename
- [ ] `src/lore_mcp/` → `src/lorme/`
  (or new name)
- [ ] All `import lore_mcp` → `import lorme`
- [ ] `pyproject.toml`: name, entry points,
  package dir
- [ ] CLI entry point: `lore-mcp` → `lorme`
- [ ] Config prefix if any

### MVP2: Repository + docs
- [ ] GitHub repo rename (Settings → rename)
- [ ] ADR-003 or ADR-005: rename decision record
- [ ] README: all references
- [ ] All docs/*.md: references
- [ ] CLAUDE.md §1, §5, §10: project name
- [ ] CONTRIBUTING.md
- [ ] examples/mcp-config.example.json
- [ ] sync/openshift.md: project name

### MVP3: External
- [ ] PyPI: publish under new name
- [ ] MCP config examples for consumers
- [ ] Linked workspace sync files

## Dependencies

- Blocks E4.02 (PyPI publish)
- No technical dependency — pure rename, no
  behavior change
- Best done before first public release (no
  users to migrate)

## Risk

**Low** — pre-release project, no external
consumers, no PyPI package published. The rename
cost is purely internal (find+replace + git).
Doing it now avoids a costly rename later with
users to migrate.
