"""
TIBET Unified CLI - The Trust Kernel for AI

Audit as a Precondition, Not an Afterthought.
"""

import click
import sys
import subprocess
from pathlib import Path

from importlib.metadata import PackageNotFoundError, version as package_version
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from .bundles import BUNDLES, FULL_PACKAGES, LEGACY_PACKAGES, PACKAGE_SPECS

console = Console()


BANNER = """
████████╗██╗██████╗ ███████╗████████╗
╚══██╔══╝██║██╔══██╗██╔════╝╚══██╔══╝
   ██║   ██║██████╔╝█████╗     ██║
   ██║   ██║██╔══██╗██╔══╝     ██║
   ██║   ██║██████╔╝███████╗   ██║
   ╚═╝   ╚═╝╚═════╝ ╚══════╝   ╚═╝
"""


DEFAULT_TIBET_HOME = Path.home() / ".tibet"


def installed_packages(package_names):
    installed = {}
    for package_name in package_names:
        try:
            installed[package_name] = package_version(package_name)
        except PackageNotFoundError:
            pass
    return installed


@click.group()
@click.version_option(package_name="tibet", prog_name="tibet")
def main():
    """TIBET - The Trust Kernel for AI.

    One install, one guided trust system: identity, provenance, continuity,
    evidence, agents, network, and conformance.

    \b
    Quick start:
      pip install -U "tibet[full]"
      tibet system doctor
      tibet system init
      tibet system walkthrough
    """
    pass


@main.command()
@click.argument("path", default=".", type=click.Path(exists=True))
@click.option("--format", "-f", type=click.Choice(["text", "json", "markdown"]), default="text")
def audit(path, format):
    """Run compliance health scan (tibet-audit).

    Scans your project for AI Act, NIS2, GDPR compliance.
    """
    try:
        cmd = ["tibet-audit", "scan", path]
        if format != "text":
            cmd.extend(["--format", format])
        subprocess.run(cmd, check=True)
    except FileNotFoundError:
        console.print("[red]tibet-audit not installed.[/red]")
        console.print("Install with: [cyan]pip install tibet[audit][/cyan]")
        sys.exit(1)


@main.command()
@click.argument("path", default=".", type=click.Path(exists=True))
def forge(path):
    """Run trust score scan (tibet-forge).

    Analyzes code quality, security, efficiency, and provenance readiness.
    """
    try:
        subprocess.run(["tibet-forge", "scan", path], check=True)
    except FileNotFoundError:
        console.print("[red]tibet-forge not installed.[/red]")
        console.print("Install with: [cyan]pip install tibet[forge][/cyan]")
        sys.exit(1)


@main.command()
@click.argument("action")
@click.option("--why", "-w", required=True, help="Intent behind this action (ERACHTER)")
@click.option("--what", "-W", default="{}", help="Content JSON (ERIN)")
@click.option("--refs", "-r", multiple=True, help="References (ERAAN)")
@click.option("--actor", "-a", default="cli", help="Who is performing this action")
def create(action, why, what, refs, actor):
    """Create a TIBET provenance token.

    Documents an action BEFORE execution with full provenance.

    Example:
        tibet create file_write --why "Fix login bug" --refs issue-123
    """
    try:
        from tibet_core import Provider
        import json

        provider = Provider(actor=actor)

        erin = json.loads(what) if what != "{}" else {}
        eraan = list(refs) if refs else []

        token = provider.create(
            action=action,
            erin=erin,
            erachter=why,
            eraan=eraan,
            eromheen={"cli": "tibet", "cwd": str(Path.cwd())}
        )

        console.print(Panel(
            f"[green]Token Created[/green]\n\n"
            f"[bold]ID:[/bold] {token.id}\n"
            f"[bold]Action:[/bold] {action}\n"
            f"[bold]Intent:[/bold] {why}\n"
            f"[bold]Actor:[/bold] {actor}",
            title="TIBET Provenance",
            border_style="green"
        ))

    except ImportError:
        console.print("[red]tibet-core not installed.[/red]")
        console.print("Install with: [cyan]pip install tibet[/cyan]")
        sys.exit(1)


@main.command()
@click.argument("token_id")
def verify(token_id):
    """Verify a TIBET token's integrity."""
    try:
        from tibet_core import Provider

        provider = Provider()
        token = provider.get(token_id)

        if not token:
            console.print(f"[red]Token not found: {token_id}[/red]")
            sys.exit(1)

        is_valid = token.verify()

        if is_valid:
            console.print(Panel(
                f"[green]✓ Token Valid[/green]\n\n"
                f"[bold]Action:[/bold] {token.action}\n"
                f"[bold]Actor:[/bold] {token.actor}\n"
                f"[bold]Created:[/bold] {token.timestamp}",
                title="Verification Result",
                border_style="green"
            ))
        else:
            console.print(Panel(
                "[red]✗ Token Invalid - Possible tampering detected[/red]",
                title="Verification Result",
                border_style="red"
            ))
            sys.exit(1)

    except ImportError:
        console.print("[red]tibet-core not installed.[/red]")
        sys.exit(1)


@main.command()
@click.option("--format", "-f", type=click.Choice(["json", "markdown", "summary"]), default="summary")
def export(format):
    """Export the full audit trail."""
    try:
        from tibet_core import Provider
        import json

        provider = Provider()
        data = provider.export()

        if format == "json":
            console.print(json.dumps(data, indent=2, default=str))
        elif format == "markdown":
            console.print("# TIBET Audit Trail\n")
            for token in data.get("tokens", []):
                console.print(f"## {token.get('action')}")
                console.print(f"- ID: `{token.get('id')}`")
                console.print(f"- Actor: {token.get('actor')}")
                console.print(f"- Intent: {token.get('erachter')}\n")
        else:
            tokens = data.get("tokens", [])
            console.print(Panel(
                f"[bold]Total Tokens:[/bold] {len(tokens)}\n"
                f"[bold]Actors:[/bold] {len(set(t.get('actor') for t in tokens))}\n"
                f"[bold]Actions:[/bold] {len(set(t.get('action') for t in tokens))}",
                title="TIBET Audit Summary",
                border_style="blue"
            ))

    except ImportError:
        console.print("[red]tibet-core not installed.[/red]")
        sys.exit(1)


@main.command()
def status():
    """Show TIBET ecosystem status — all bundles and components."""
    console.print(BANNER, style="cyan")
    console.print("[bold]The Trust Kernel for AI[/bold]")
    console.print("[dim]One install, one guided trust system.[/dim]\n")

    installed = installed_packages(FULL_PACKAGES)
    total = len(FULL_PACKAGES)
    found = len(installed)

    console.print(f"[bold green]{found}[/bold green]/{total} components installed\n")

    # Show per bundle
    for bundle_name, bundle_info in BUNDLES.items():
        bundle_pkgs = bundle_info["packages"]
        bundle_installed = sum(1 for p in bundle_pkgs if p in installed)
        bundle_total = len(bundle_pkgs)

        if bundle_installed == bundle_total:
            icon = "[green]■[/green]"
            label = f"[green]{bundle_name}[/green]"
        elif bundle_installed > 0:
            icon = "[yellow]◧[/yellow]"
            label = f"[yellow]{bundle_name}[/yellow]"
        else:
            icon = "[dim]□[/dim]"
            label = f"[dim]{bundle_name}[/dim]"

        parts = []
        for p in bundle_pkgs:
            if p in installed:
                parts.append(f"[green]{p}[/green]")
            else:
                parts.append(f"[dim]{p}[/dim]")

        console.print(f"  {icon} {label} ({bundle_installed}/{bundle_total}) — {bundle_info['desc']}")
        console.print(f"    {' '.join(parts)}")
        if bundle_installed < bundle_total:
            console.print(Text(f"    {bundle_info['install']}", style="dim"))
        console.print()

    console.print(Text('pip install -U "tibet[full]"  — install the full trust system', style="dim"))
    console.print("[dim]tibet system doctor          — validate the local system[/dim]")
    console.print("[dim]One love, one fAmIly![/dim]")


@main.command()
@click.argument("path", default=".", type=click.Path())
def init(path):
    """Initialize TIBET in a project.

    Creates .tibet/ directory for local token storage.
    """
    tibet_dir = Path(path) / ".tibet"
    tibet_dir.mkdir(exist_ok=True)

    config_file = tibet_dir / "config.json"
    if not config_file.exists():
        import json
        config = {
            "version": "1.0.0",
            "actor": "local",
            "store": "file",
            "created": str(Path.cwd())
        }
        config_file.write_text(json.dumps(config, indent=2))

    console.print(Panel(
        f"[green]TIBET initialized in {path}[/green]\n\n"
        f"Created: .tibet/config.json\n\n"
        f"Next steps:\n"
        f"  tibet audit    - Scan for compliance\n"
        f"  tibet forge    - Check trust score\n"
        f"  tibet create   - Create provenance token",
        title="TIBET Init",
        border_style="green"
    ))


@main.command()
def bundles():
    """Show available installation bundles."""
    console.print("[bold]TIBET Installation Bundles[/bold]\n")

    table = Table()
    table.add_column("Bundle", style="cyan")
    table.add_column("Packages", style="dim")
    table.add_column("Install", style="green")

    for name, info in BUNDLES.items():
        table.add_row(
            f"{name}\n[dim]{info['desc']}[/dim]",
            "\n".join(info["packages"]),
            Text(info["install"], style="green"),
        )

    table.add_row(
        "[bold]full[/bold]\n[dim]The complete trust system[/dim]",
        "\n".join(FULL_PACKAGES),
        Text('pip install "tibet[full]"', style="bold green"),
    )

    console.print(table)


@main.group()
def system():
    """Initialize, validate and update the local TIBET system."""
    pass


@system.command("doctor")
def system_doctor():
    """Validate the installed TIBET system."""
    installed = installed_packages(FULL_PACKAGES)
    missing = [name for name in FULL_PACKAGES if name not in installed]
    legacy_installed = [name for name in LEGACY_PACKAGES if name in installed_packages(LEGACY_PACKAGES)]

    table = Table(title="TIBET System Doctor")
    table.add_column("Check", style="cyan")
    table.add_column("Result")

    table.add_row("Full package set", f"{len(installed)}/{len(FULL_PACKAGES)} installed")
    table.add_row("Missing packages", ", ".join(missing) if missing else "[green]none[/green]")
    table.add_row("Legacy packages", ", ".join(legacy_installed) if legacy_installed else "[green]none active[/green]")

    tibet_home = DEFAULT_TIBET_HOME
    table.add_row("TIBET home", str(tibet_home) if tibet_home.exists() else f"[yellow]missing: {tibet_home}[/yellow]")

    for dirname in ["inbox", "outbox", "audit", "reports", "state"]:
        path = tibet_home / dirname
        table.add_row(f"Directory {dirname}", "[green]ok[/green]" if path.exists() else "[yellow]missing[/yellow]")

    console.print(table)

    if missing:
        console.print()
        console.print(Text('Next: pip install -U "tibet[full]"', style="yellow"))
    if not tibet_home.exists():
        console.print("[yellow]Next:[/yellow] tibet system init")


@system.command("init")
@click.option("--home", type=click.Path(path_type=Path), default=DEFAULT_TIBET_HOME)
def system_init(home):
    """Create the local TIBET system directories and default config."""
    import json

    home.mkdir(parents=True, exist_ok=True)
    for dirname in ["inbox", "outbox", "audit", "reports", "state"]:
        (home / dirname).mkdir(exist_ok=True)

    config_path = home / "config.json"
    if not config_path.exists():
        config = {
            "version": "1.0",
            "home": str(home),
            "osapi": {
                "tibet": "127.0.0.1:18443",
                "jis": "127.0.0.1:18444",
            },
            "soft_bootstrap_env": "TIBET_SOFT_BOOTSTRAP",
            "event_log": "/var/log/tibet/gateway.jsonl",
        }
        config_path.write_text(json.dumps(config, indent=2) + "\n")

    console.print(Panel(
        f"[green]TIBET system initialized[/green]\n\n"
        f"Home: {home}\n"
        f"Config: {config_path}\n\n"
        f"Next:\n"
        f"  tibet system doctor\n"
        f"  tibet system walkthrough",
        title="TIBET System",
        border_style="green",
    ))


@system.command("walkthrough")
def system_walkthrough():
    """Show the first-run path after installing tibet[full]."""
    steps = [
        ("1", "Install/update", 'pip install -U "tibet[full]"'),
        ("2", "Validate", "tibet system doctor"),
        ("3", "Initialize", "tibet system init"),
        ("4", "Bind identity", "jis claim && tibet create system_boot --why \"Initialize local trust system\""),
        ("5", "Check reachability", "tibet-ping local && ipoll status"),
        ("6", "Create evidence", "tibet audit . && tibet system doctor"),
        ("7", "Start operations", "Use Cmail/cap-bus/gateway events when available"),
    ]

    table = Table(title="TIBET First-Run Walkthrough")
    table.add_column("#", style="cyan")
    table.add_column("Goal")
    table.add_column("Command")
    for step, goal, command in steps:
        table.add_row(step, goal, Text(command))
    console.print(table)


@system.command("update")
@click.option("--execute", is_flag=True, help="Actually run pip install -U tibet[full].")
def system_update(execute):
    """Prepare or run a full-system package update."""
    cmd = [sys.executable, "-m", "pip", "install", "-U", "tibet[full]"]
    if not execute:
        console.print("[yellow]Dry run only.[/yellow] Use --execute to run:")
        console.print(" ".join(cmd), markup=False)
        console.print("Then run: tibet system doctor")
        return
    subprocess.run(cmd, check=True)
    console.print("[green]Update completed.[/green] Run: tibet system doctor")


@main.command()
def version():
    """Show versions of all installed TIBET components."""
    installed = installed_packages(["tibet"] + FULL_PACKAGES)
    for pkg_name, ver in installed.items():
        console.print(f"{pkg_name}: [cyan]{ver}[/cyan]")


if __name__ == "__main__":
    main()
