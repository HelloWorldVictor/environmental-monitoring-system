import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from alerter import check_thresholds
from api_handler import fetch_and_parse_data
from db_handler import save_data


console = Console()


def clear_screen():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def print_header():
    """Prints the application header with rich styling."""
    clear_screen()
    header_text = Text("ENVIRONMENTAL MONITORING – CLI v1.0", style="bold yellow")
    panel = Panel(header_text, border_style="blue", width=50, highlight=True)
    console.print(panel, justify="center")


def print_menu():
    """Prints the main menu options with rich styling."""
    menu = Text()
    menu.append("\n[1] ", style="bold green")
    menu.append("Fetch & Log Current Data\n")
    menu.append("[2] ", style="bold green")
    menu.append("Show Latest Readings\n")
    menu.append("[3] ", style="bold green")
    menu.append("Query Historical Data\n")
    menu.append("[4] ", style="bold green")
    menu.append("Set Safety Thresholds\n")
    menu.append("[5] ", style="bold green")
    menu.append("View Health & Safety Tips\n")
    menu.append("[6] ", style="bold red")
    menu.append("Exit")

    console.print(menu, justify="left")
    console.print("-" * 50, style="dim")


def handle_fetch_data():
    """Handles fetching, saving, and alerting on new data."""
    clear_screen()
    console.print("\n[bold blue]Fetching latest environmental data...[/bold blue]")

    try:
        data = fetch_and_parse_data()
        save_data(data)
        console.print(
            "[bold green]Data successfully logged to the database.[/bold green]"
        )

        alerts = check_thresholds(data)
        if alerts:
            for alert in alerts:
                console.print(f"[bold red]{alert}[/bold red]")
        else:
            console.print(
                "[bold green]All readings are within safe limits.[/bold green]"
            )
    except Exception as e:
        console.print(f"[bold red]An error occurred: {e}[/bold red]")
