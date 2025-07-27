import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text


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
