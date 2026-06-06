"""Canonical install bundles for the TIBET umbrella package.

This file is the single package-level map used by the sandbox proposal for
``pip install tibet[full]`` and the CLI status/doctor commands.
"""

PACKAGE_SPECS = {
    "tibet-core": "tibet-core>=0.5.0",
    "jis-core": "jis-core>=0.4.0",
    "tibet-audit": "tibet-audit>=0.27.1",
    "tibet-continuityd": "tibet-continuityd>=0.6.17",
    "tibet-cbom": "tibet-cbom>=0.2.2",
    "tibet-sbom": "tibet-sbom>=0.2.1",
    "tibet-ai-sbom": "tibet-ai-sbom>=0.2.2",
    "ai-sbom": "ai-sbom>=0.1.3",
    "tibet-wayback": "tibet-wayback>=0.2.1",
    "tibet-nis2": "tibet-nis2>=0.1.1",
    "tibet-report": "tibet-report>=0.1.2",
    "tibet-trail": "tibet-trail>=0.1.1",
    "tibet-ci": "tibet-ci>=0.2.1",
    "ainternet": "ainternet>=0.9.2",
    "ipoll": "ipoll>=0.2.6",
    "tibet-ainternet-mcp": "tibet-ainternet-mcp>=0.5.7",
    "tibet-ipoll-mcp": "tibet-ipoll-mcp>=0.1.0",
    "tibet-triage": "tibet-triage>=0.5.2",
    "tibet-airlock": "tibet-airlock>=0.3.1",
    "tibet-phantom": "tibet-phantom>=0.2.2",
    "tibet-phantom-mcp": "tibet-phantom-mcp>=0.1.1",
    "tibet-cap-bus": "tibet-cap-bus>=0.1.4",
    "tibet-context": "tibet-context>=0.2.2",
    "tibet-cortex": "tibet-cortex>=0.2.1",
    "tibet-router": "tibet-router>=0.1.2",
    "tibet-cobol": "tibet-cobol>=0.1.1",
    "snaft": "snaft>=1.4.1",
    "tibet-chip": "tibet-chip>=1.0.1",
    "tibet-claw": "tibet-claw>=0.3.2",
    "tibet-gateway": "tibet-gateway>=0.4.0",
    "tibet-home-agent": "tibet-home-agent>=0.5.3",
    "tibet-pol": "tibet-pol>=0.3.4",
    "tibet-ping": "tibet-ping>=0.3.4",
    "tibet-mux": "tibet-mux>=1.0.2",
    "tibet-overlay": "tibet-overlay>=0.1.2",
    "tibet-iot": "tibet-iot>=0.1.1",
    "tibet-edge": "tibet-edge>=0.1.1",
    "tibet-mesh": "tibet-mesh>=0.1.0",
    "tibet-zip": "tibet-zip>=1.1.1",
    "tibet-spiffe": "tibet-spiffe>=0.1.1",
    "tibet-tools": "tibet-tools>=0.1.1",
    "tibet-marketplace": "tibet-marketplace>=0.1.1",
    "tibet-nc": "tibet-nc>=0.1.2",
    "tibet-keychain": "tibet-keychain>=0.1.2",
    "tibet-tail": "tibet-tail>=0.2.1",
    "tibet-soc": "tibet-soc>=0.1.1",
    "tibet-conformance-vectors": "tibet-conformance-vectors>=0.2.2",
    "tibet-forge": "tibet-forge>=0.7.1",
    "tibet-vault": "tibet-vault>=0.1.0",
    "tibet-pqc": "tibet-pqc>=0.1.1",
    "tibet-anticheat": "tibet-anticheat>=0.1.2",
    "tibet-y2k38": "tibet-y2k38>=0.1.2",
    "tibet-pol-mcp": "tibet-pol-mcp>=0.1.0",
    "tibet-triage-mcp": "tibet-triage-mcp>=0.1.0",
    "tibet-cmail": "tibet-cmail>=0.3.0",
    "tibet-genesis": "tibet-genesis>=0.1.4",
}

PACKAGE_IMPORTS = {
    name: name.replace("-", "_")
    for name in PACKAGE_SPECS
}
PACKAGE_IMPORTS.update({
    "ai-sbom": "ai_sbom",
    "jis-core": "jis_core",
})

LEGACY_PACKAGES = {
    "tibet-snap": "Replaced by continuityd/wayback/phantom resume flows.",
}

BUNDLES = {
    "core": {
        "desc": "Identity + provenance handshake substrate",
        "packages": ["tibet-core", "jis-core"],
        "install": 'pip install "tibet[core]"',
    },
    "daemon": {
        "desc": "Background guardians and continuity",
        "packages": ["tibet-continuityd", "tibet-gateway", "tibet-cap-bus", "tibet-home-agent"],
        "install": 'pip install "tibet[daemon]"',
    },
    "evidence": {
        "desc": "SBOM/CBOM, audit trail, reports and replay",
        "packages": [
            "tibet-audit",
            "tibet-sbom",
            "tibet-cbom",
            "tibet-ai-sbom",
            "ai-sbom",
            "tibet-wayback",
            "tibet-report",
            "tibet-trail",
            "tibet-nis2",
            "tibet-cmail",
            "tibet-ci",
        ],
        "install": 'pip install "tibet[evidence]"',
    },
    "agentic": {
        "desc": "Agent communication, MCP surfaces and session resume",
        "packages": [
            "ainternet",
            "ipoll",
            "tibet-ainternet-mcp",
            "tibet-ipoll-mcp",
            "tibet-phantom",
            "tibet-phantom-mcp",
            "tibet-context",
            "tibet-cortex",
            "tibet-router",
            "tibet-cobol",
        ],
        "install": 'pip install "tibet[agentic]"',
    },
    "safety": {
        "desc": "Isolation, triage and active immune-system controls",
        "packages": [
            "snaft",
            "tibet-airlock",
            "tibet-triage",
            "tibet-chip",
            "tibet-claw",
            "tibet-genesis",
            "tibet-pqc",
            "tibet-anticheat",
            "tibet-y2k38",
        ],
        "install": 'pip install "tibet[safety]"',
    },
    "operator": {
        "desc": "Human-facing operational tools",
        "packages": [
            "tibet-pol",
            "tibet-ping",
            "tibet-tools",
            "tibet-marketplace",
            "tibet-nc",
            "tibet-keychain",
            "tibet-tail",
            "tibet-soc",
        ],
        "install": 'pip install "tibet[operator]"',
    },
    "network": {
        "desc": "Mesh, mux, overlay and edge transport",
        "packages": [
            "tibet-mux",
            "tibet-overlay",
            "tibet-iot",
            "tibet-edge",
            "tibet-mesh",
            "tibet-zip",
            "tibet-spiffe",
        ],
        "install": 'pip install "tibet[network]"',
    },
    "conformance": {
        "desc": "Contract vectors and MCP conformance helpers",
        "packages": ["tibet-conformance-vectors", "tibet-triage-mcp", "tibet-pol-mcp"],
        "install": 'pip install "tibet[conformance]"',
    },
    "legacy": {
        "desc": "Compatibility packages kept out of full installs",
        "packages": ["tibet-snap"],
        "install": 'pip install "tibet[legacy]"',
    },
}

FULL_BUNDLE_NAMES = [
    "core",
    "daemon",
    "evidence",
    "agentic",
    "safety",
    "operator",
    "network",
    "conformance",
]

FULL_PACKAGES = []
for bundle_name in FULL_BUNDLE_NAMES:
    for package_name in BUNDLES[bundle_name]["packages"]:
        if package_name not in FULL_PACKAGES:
            FULL_PACKAGES.append(package_name)


def specs_for(package_names):
    """Return dependency specifiers for package names in order."""
    return [PACKAGE_SPECS[name] for name in package_names]
