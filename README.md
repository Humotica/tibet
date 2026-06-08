# tibet

The Humotica trust-system profile installer. Install only the layer you need:
zero-state bootstrap, continuity, network, operator tools, observability,
AI governance, firewall, evidence, compliance, agents, and conformance.

[![PyPI](https://img.shields.io/pypi/v/tibet)](https://pypi.org/project/tibet/)
[![IETF Draft](https://img.shields.io/badge/IETF-draft--vandemeent--tibet--provenance-blue)](https://datatracker.ietf.org/doc/draft-vandemeent-tibet-provenance/)
[![Whitepaper](https://img.shields.io/badge/Zenodo-DOI:10.5281/zenodo.18712238-green)](https://doi.org/10.5281/zenodo.18712238)

Unified CLI for [tibet-core](https://pypi.org/project/tibet-core/) provenance,
[jis-core](https://pypi.org/project/jis-core/) identity, evidence generation,
agent communication, and first-run system setup.

## Install

```bash
pip install tibet                    # CLI + tibet-core + jis-core
pip install "tibet[zero-state]"      # T-1 bootstrap: JIS, TIBET, genesis, causal time
pip install "tibet[runtime]"         # zero-state + continuity + network + operator
pip install "tibet[observability]"   # cascade logging, tail, trail, ping, pol
pip install "tibet[governed-ai]"     # AI governance + firewall + agent + evidence
pip install "tibet[enterprise]"      # runtime + security + evidence + compliance
pip install "tibet[full]"            # supported full profile, no deprecated/niche extras
pip install "tibet[lab]"             # research/lab profile with legacy and niche adapters
```

## After Install

```bash
tibet system doctor
tibet system init
tibet system walkthrough
```

`tibet[full]` is the supported full profile. Deprecated aliases, marketplace
tooling, COBOL, SPIFFE, Y2K38, anti-cheat, and other niche adapters are opt-in
through `tibet[legacy]`, `tibet[interop]`, `tibet[tooling]`, or `tibet[lab]`.

The canonical profiles are:

- `zero-state`: T-1 bootstrap, JIS identity, TIBET provenance, genesis, causal time
- `continuity`: continuityd, cap-bus, CBOM, trail, wayback, Phantom state-resume/fork
- `network`: ping, overlay, mux, nc, mesh, tibet-zip
- `operator`: policy, tail, Cmail, keychain, home-agent
- `observability`: Cascade Logging via `tibet-cascade`, tail, trail, ping, pol
- `ai-governance`: airlock, triage, claw, cortex, SAM
- `firewall`: SNAFT, tibet-snaft, inject-bender
- `security`: AI governance + firewall + PQC + gateway
- `evidence`: audit, SBOM, AI-SBOM, report, wayback, trail
- `compliance`: NIS2, CI, SOC, workload attestation
- `agent`: AInternet, I-Poll, MCP surfaces, Phantom, context
- `conformance`: public contract vectors and MCP checks

## Quick Start

```bash
# Initialize TIBET in your project.
tibet init

# Create a provenance token. Document before you act.
tibet create deploy --why "Release v1.0.0" --refs ticket-123

# Verify token integrity.
tibet verify <token-id>

# Export audit trail.
tibet export --format json

# Run compliance scan.
tibet audit

# Check trust score.
tibet forge

# Show installed components.
tibet status
```

## Commands

| Command | Description |
|---------|-------------|
| `tibet init` | Initialize `.tibet/` directory for local token storage |
| `tibet create <action>` | Create provenance token with intent (`--why`), content (`--what`), and references (`--refs`) |
| `tibet verify <id>` | Verify a token's cryptographic integrity |
| `tibet export` | Export audit trail (JSON, markdown, or summary) |
| `tibet audit` | Run compliance health scan — AI Act, NIS2, GDPR (requires `tibet[audit]`) |
| `tibet forge` | Run trust score analysis — code quality, security, provenance readiness (requires `tibet[forge]`) |
| `tibet status` | Show ecosystem status and installed component versions |
| `tibet system doctor` | Validate the local full-system install |
| `tibet system init` | Create `~/.tibet/` config, inbox, outbox, audit, reports, and state dirs |
| `tibet system walkthrough` | Show the guided first-run path after `tibet[full]` |
| `tibet system update` | Show or execute the explicit full-system update command |
| `tibet version` | Show versions of all TIBET components |

### Creating Tokens

Every token captures four provenance dimensions:

```bash
tibet create file_write \
  --why "Fix login bug"          \  # ERACHTER — intent
  --what '{"file":"auth.py"}'    \  # ERIN — content
  --refs issue-123               \  # ERAAN — references
  --actor "jis:dev:alice"           # Who
```

The token is created BEFORE the action happens. This is structural — provenance that's recorded after the fact is just logging.

## TIBET Provenance

Every token records four dimensions:

| Dimension | Dutch | Meaning |
|-----------|-------|---------|
| **ERIN** | "Er in" | What's IN the action (content, data) |
| **ERAAN** | "Er aan" | What's attached (dependencies, references) |
| **EROMHEEN** | "Er omheen" | Context around it (environment, state) |
| **ERACHTER** | "Er achter" | Intent behind it (why this action) |

## Ecosystem

`tibet` is the CLI. The kernel is [tibet-core](https://pypi.org/project/tibet-core/). Together with the rest of the stack:

| Layer | Package | What it does |
|-------|---------|--------------|
| **Identity** | [jis-core](https://pypi.org/project/jis-core/) | Claims and identity binding |
| **Provenance** | [tibet-core](https://pypi.org/project/tibet-core/) | TIBET tokens — ERIN/ERAAN/EROMHEEN/ERACHTER |
| **CLI** | **tibet** | `tibet system`, `tibet create`, `tibet verify`, `tibet audit`, `tibet forge` |
| **Firewall** | [snaft](https://pypi.org/project/snaft/) | 22 immutable rules, OWASP 20/20, FIR/A trust |
| **Network** | [ainternet](https://pypi.org/project/ainternet/) | .aint domains, I-Poll messaging, agent discovery |
| **Home Agent** | [tibet-home-agent](https://pypi.org/project/tibet-home-agent/) | Headless agent relay with HITL approval path |
| **Cmail** | [tibet-cmail](https://pypi.org/project/tibet-cmail/) | Capsules, acknowledgements, and signed approval mail |
| **Compliance** | [tibet-audit](https://pypi.org/project/tibet-audit/) | AI Act, NIS2, GDPR, CRA — 112+ checks |
| **Trust** | [tibet-forge](https://pypi.org/project/tibet-forge/) | Trust scoring and certification |
| **SBOM** | [tibet-sbom](https://pypi.org/project/tibet-sbom/) | Supply chain verification with provenance |
| **CBOM** | [tibet-cbom](https://pypi.org/project/tibet-cbom/) | Capability bill of materials |
| **Continuity** | [tibet-continuityd](https://pypi.org/project/tibet-continuityd/) | Background continuity guardian |
| **Capability Bus** | [tibet-cap-bus](https://pypi.org/project/tibet-cap-bus/) | Gateway event contract and command bus |
| **Cascade Logging** | [tibet-cascade](https://pypi.org/project/tibet-cascade/) | Causal observability across JIS, TIBET, cap-bus, network, continuity, Phantom, and evidence |
| **Triage** | [tibet-triage](https://pypi.org/project/tibet-triage/) | Airlock sandbox, UPIP reproducibility, flare rescue |
| **Transfer** | [tibet-zip](https://pypi.org/project/tibet-zip/) | Identity-aware signed transfer container |
| **Netcat** | [tibet-nc](https://pypi.org/project/tibet-nc/) | Operator-friendly network command tooling |
| **Secrets** | [tibet-vault](https://pypi.org/project/tibet-vault/) | Time-locked secrets with dead man's switch |
| **Discovery** | [tibet-ping](https://pypi.org/project/tibet-ping/) | LAN discovery, heartbeat, mesh relay |

## Standards

### IETF Standardization

- [draft-vandemeent-tibet-provenance](https://datatracker.ietf.org/doc/draft-vandemeent-tibet-provenance/) — Traceable Intent-Based Event Tokens
- [draft-vandemeent-jis-identity](https://datatracker.ietf.org/doc/draft-vandemeent-jis-identity/) — JTel Identity Standard
- [draft-vandemeent-upip-process-integrity](https://datatracker.ietf.org/doc/draft-vandemeent-upip-process-integrity/) — Universal Process Integrity Protocol
- [draft-vandemeent-rvp-continuous-verification](https://datatracker.ietf.org/doc/draft-vandemeent-rvp-continuous-verification/) — Real-time Verification Protocol
- [draft-vandemeent-ains-discovery](https://datatracker.ietf.org/doc/draft-vandemeent-ains-discovery/) — AInternet Name Service

### Regulatory

| Regulation | TIBET provides |
|------------|---------------|
| **EU AI Act** | Automated decision traceability, transparency |
| **EU CRA** | Build provenance, SBOM accountability |
| **GDPR Art. 22** | Consent proof, decision audit trail |
| **NIS2** | Continuous logging, incident snapshots |

CRA enforcement starts **September 2026**. TIBET makes compliance architectural, not bolted-on.

## License

MIT

## Credits

Designed by [Jasper van de Meent](https://github.com/jaspertvdm). Built by Jasper and [Root AI](https://humotica.com) as part of [HumoticaOS](https://humotica.com).

One love, one fAmIly.


---

**Stack-positie:** Groep `substrate` · Bootstrap = OSAPI-handshake naar [`tibet`](https://pypi.org/project/tibet-core/) + [`jis`](https://pypi.org/project/jis-core/) (fail → snaft-rule + tibet-pol-rapport) · ← [`tibet-core`](https://pypi.org/project/tibet-core/) · See `STACK.md` · See `demo/golden-path/` for the spine end-to-end.
---

## Enterprise

For private hub hosting, SLA support, custom integrations, or compliance guidance:

| | |
|---|---|
| **Enterprise** | enterprise@humotica.com |
| **Support** | support@humotica.com |
| **Security** | security@humotica.com |

See [ENTERPRISE.md](ENTERPRISE.md) for details.
