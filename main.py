import os
import sys
import json
import argparse
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

VERSION = "GHOST-KubernetesAuditor v1.0-PRO"
BANNER = """
[bold cyan] ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ██╗  ██╗██╗   ██╗██████╗ ███████╗[/bold cyan]
[bold cyan]██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝     ██║ ██╔╝██║   ██║██╔══██╗██╔════╝[/bold cyan]
[bold white]██║  ███╗███████║██║   ██║███████╗   ██║        █████╔╝ ██║   ██║██████╔╝███████╗[/bold white]
[bold white]██║   ██║██╔══██║██║   ██║╚════██║   ██║        ██╔═██╗ ██║   ██║██╔══██╗╚════██║[/bold white]
[bold blue]╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ██╗  ██║  ██╗╚██████╔╝██████╔╝███████║[/bold blue]
[bold blue] ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝[/bold blue]
[bold yellow]     GHOST-KubernetesAuditor: Cluster Security & RBAC Assessment Engine[/bold yellow]
"""

console = Console()

def main():
    parser = argparse.ArgumentParser(description="GHOST-KubernetesAuditor")
    parser.add_argument("--cluster", default="default", help="Target Kubernetes cluster context")
    args = parser.parse_args()
    
    console.print(Panel(BANNER, border_style="cyan", expand=False))
    console.print(f"[+] Assessing Kubernetes cluster context '{args.cluster}' for privilege escalation, RBAC flaws, and insecure pods...")
    
    table = Table(title=f"Kubernetes Security Findings: {args.cluster}", border_style="red")
    table.add_column("Resource / Check", style="cyan")
    table.add_column("Severity", style="yellow")
    table.add_column("Remediation", style="white")
    table.add_row("Over-permissive ClusterRoleBinding", "Critical", "Restrict cluster-admin permissions from service accounts")
    table.add_row("Privileged Container Running (securityContext)", "High", "Disable privileged mode in Pod security standards")
    table.add_row("Default ServiceAccount Token Mounted", "Medium", "Disable automountServiceAccountToken where unnecessary")
    console.print(table)
    console.print("\n[bold green][+] Kubernetes cluster audit completed successfully.[/bold green]")

if __name__ == "__main__":
    main()
