# Changelog — `tibet` (meta-installer)

## 2.1.2 — 2026-05-28 (later same day)

### Fixed
- **`tibet --version` showed `2.0.1` instead of the installed version** — hardcoded `@click.version_option(version="2.0.1", ...)` was missed during the 2.1.0/2.1.1 merge. Switched to `package_name="tibet"` so Click auto-resolves via `importlib.metadata`. From now on every release reports its own version.

## 2.1.1 — 2026-05-28

### Fixed
- `tibet-triage-mcp` lower-bound was `>=0.1.1`; PyPI only has 0.1.0. Patched to `>=0.1.0` so `pip install "tibet[full]"` resolves cleanly.

## 2.1.0 — 2026-05-28

The fork → main move for the meta-installer. `pip install "tibet[full]"` is no longer a stale April-bundle — it is now a **guided local trust-system install** built around the v1.0 OSAPI-pair.

### Added
- **`tibet system` CLI-group**: `doctor` / `init` / `walkthrough` / `update`. `tibet[full]` is now a real system-installer, not a dependency dump.
- **`src/tibet/bundles.py`** — single canonical bundle-map used by both `pyproject.toml` and the CLI (no more drift between deps and `tibet bundles` output).
- New role-based optional-dependency-groups: `core` / `daemon` / `evidence` / `agentic` / `safety` / `operator` / `network` / `conformance` / `legacy` / `full`.
- Post-april packages added to `full`: `jis-core`, `tibet-continuityd`, `tibet-cap-bus`, `tibet-cbom`, `tibet-ai-sbom` (+ `ai-sbom`), `tibet-wayback`, `tibet-report`, `tibet-trail`, `tibet-nis2`, `tibet-gateway`, `tibet-ipoll-mcp`, `tibet-tools`, `tibet-marketplace`, `tibet-context`, `tibet-chip`, `tibet-claw`, `tibet-conformance-vectors`, `tibet-triage-mcp`, `tibet-pol-mcp`, `tibet-iot`, `tibet-edge`, `tibet-mesh`.
- README reframed: from "dependency bundle" to "Humotica trust-system installer" with the after-install path (`doctor → init → walkthrough`).

### Changed
- **`tibet-core>=0.5.0b2`** is now the baseline (was 0.4.0); pulls in the OSAPI bootstrap-pair + emit-hook.
- **`jis-core>=0.4.0b1`** added to `core` and `full` — bootstrap-pair completed (identity + provenance).

### Removed from `full`
- `tibet-snap` — moved to `legacy`-only. Continuity/wayback/phantom-resume flows replace it (per STACK.md).

### Discipline (cross-package)
- Bundles align with the canonical groups in `STACK.md` (substrate/evidence/agentic/safety/conformance + meta).
- Every non-kernel package in `full` is expected to declare `tibet-core` + `jis-core` as runtime-deps and bootstrap to the OSAPI-pair (the no-fail-open "vanaf nu mee" discipline). Roll-out starts with `tibet-audit` as first-mover.

### Credits
Bundle map and `tibet system` CLI prepared by Codex (sandbox workcopy 2026-05-28), reviewed + merged + bumped + uploaded by Root AI.

## 2.0.1 — earlier (April 2026)

Stale April-snapshot. Missed all post-april packages (continuityd, cbom, ai-sbom, vault, gateway, cap-bus, etc.) — the gap that v2.1 closes.
