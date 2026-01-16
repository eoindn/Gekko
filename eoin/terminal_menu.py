import sys
from main import anaylse_file, calculate_entropy,string_dump, analyse_sections
import os
from colorama import Back, Fore, Style
import math
from collections import Counter
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich import box
from rich.text import Text
from rich import print

console = Console()


def print_banner():
    banner = """
    ██████╗ ███████╗██╗  ██╗██╗  ██╗ ██████╗ 
   ██╔════╝ ██╔════╝██║ ██╔╝██║ ██╔╝██╔═══██╗
   ██║  ███╗█████╗  █████╔╝ █████╔╝ ██║   ██║
   ██║   ██║██╔══╝  ██╔═██╗ ██╔═██╗ ██║   ██║
   ╚██████╔╝███████╗██║  ██╗██║  ██╗╚██████╔╝
    ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ 
    """
    
    panel = Panel(
        banner,
        title="[bold green]GEKKO[/bold green]",
        subtitle="[cyan]Malware Analysis Pipeline v1.0[/cyan]",
        border_style="green",
        box=box.DOUBLE
    )
    console.print(panel)





def show_menu():
    """Display available commands"""
    table = Table(title="Available Commands", box=box.ROUNDED)
    table.add_column("Command", style="cyan", no_wrap=True)
    table.add_column("Description", style="white")
    
    table.add_row("analyse", "Run full analysis on file")
    table.add_row("entropy", "Calculate file entropy")
    table.add_row("strings", "Dump strings from file")
    table.add_row("sections", "Show PE sections (if PE file)")
    table.add_row("sections-analyse", "Analyse PE sections for anomalies")
    table.add_row("help", "Show this menu")
    table.add_row("exit", "Exit program")
    
    console.print(table)




def main():
    if len(sys.argv) > 2:
        console.print("[red]Usage: python menu.py <filename> [/red]")
        sys.exit(1)
    global filename
    filename = sys.argv[1]
    if not os.path.exists(filename):
        console.print(f"[red]Error: {filename} not found [/red] ")
        sys.exit(1)

    print_banner()
    show_menu()
    filesize = os.path.getsize(filename)
    print(f"[bold green]Loaded file:[/bold green] [white]{filename}[/white] \n[green]{filesize}[/green] bytes")


main()

while True:
    try:
        command = Prompt.ask("\n[bold cyan]gekko>[/bold cyan]").strip().lower()

        if command == "exit":
            print("[yellow]Exiting Gekko[/yellow]")
            break

        elif command == "help":
            show_menu()

        
        elif command == "analyse":
            anaylse_file(filename)

        elif command == "strings":
            string_dump(filename)

        elif command == "sections-analyse":
            analyse_sections(filename)
        
        elif command == "entropy":
            result = calculate_entropy(filename)
            if result > 7:
                console.print("[red]High entropy detected! Possible packed or encrypted file.[/red]")
            else:
                console.print(f"[green]Normal Entropy: {result}[/green]")

        else:
            console.print(f"[red]Unknown command: '{command}'. Type 'help' for available commands.[/red]")
        

        

    except KeyboardInterrupt:
            console.print("\n[yellow]Interrupted. Type 'exit' to quit.[/yellow]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

        

