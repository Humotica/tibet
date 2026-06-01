"""
TIBET - The Trust Kernel for AI
================================

Audit as a Precondition, Not an Afterthought.

Unified CLI for the complete TIBET ecosystem:
- tibet-core: Provenance tokens
- tibet-audit: Compliance scanning
- tibet-forge: Trust scoring
- tibet-vault: Time-locked secrets

Usage:
    tibet init          Initialize TIBET in project
    tibet audit         Run compliance scan
    tibet forge         Run trust score scan
    tibet create        Create provenance token
    tibet verify        Verify token integrity
    tibet status        Show TIBET status

Philosophy:
- ERIN: What's IN the action (content)
- ERAAN: What's attached (dependencies)
- EROMHEEN: Context around it (environment)
- ERACHTER: Intent behind it (why)

Part of HumoticaOS - One love, one fAmIly!
"""

__version__ = "1.0.1"

# Try to import components
try:
    from tibet_core import Provider, Token
except ImportError:
    Provider = None
    Token = None

try:
    from tibet_audit import scan as audit_scan
except ImportError:
    audit_scan = None

try:
    from tibet_forge import scan as forge_scan
except ImportError:
    forge_scan = None

__all__ = ["__version__", "Provider", "Token", "audit_scan", "forge_scan"]
