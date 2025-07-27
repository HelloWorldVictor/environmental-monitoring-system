from datetime import datetime
import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

from alerter import check_thresholds
from api_handler import fetch_and_parse_data
from db_handler import get_historical_data, get_latest_readings, save_data


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

def handle_show_latest():
    """Handles displaying the most recent readings."""
    clear_screen()
    console.print("\n[bold blue]Fetching latest readings...[/bold blue]")
    readings = get_latest_readings()
    if not readings:
        console.print("[bold yellow]No data available. Fetch data first.[/bold yellow]")
        return

    table = Table(title="Latest Environmental Readings", style="cyan")
    table.add_column("Metric", style="bold")
    table.add_column("Value", style="green")
    table.add_column("Timestamp", style="dim")

    timestamp = readings.get("timestamp", "N/A")

    table.add_row(
        "Temperature", f"{readings.get('temperature', 'N/A'):.2f} °C", timestamp
    )

    def safe_format(value, fmt, default="N/A"):
        try:
            if value is None:
                return default
            return fmt.format(value)
        except Exception:
            return default

    table.add_row(
        "Humidity", safe_format(readings.get("humidity"), "{:.2f} %"), timestamp
    )
    table.add_row("CO2", safe_format(readings.get("co2"), "{:.2f} ppm"), timestamp)
    table.add_row("CO", safe_format(readings.get("co"), "{:.3f} ppm"), timestamp)
    table.add_row("PM2.5", safe_format(readings.get("pm25"), "{:.2f} µg/m³"), timestamp)
    table.add_row("PM10", safe_format(readings.get("pm10"), "{:.2f} µg/m³"), timestamp)

    console.print(table)

def handle_query_historical():
    """Handles querying and displaying historical data."""
    clear_screen()
    console.print("\n[bold blue]Query historical data:[/bold blue]")

    try:
        start_str = console.input("[bold]Enter start date (YYYY-MM-DD): [/bold]")
        end_str = console.input("[bold]Enter end date (YYYY-MM-DD): [/bold]")
        start_date = datetime.strptime(start_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_str, "%Y-%m-%d")

        data = get_historical_data(start_date, end_date)
        if not data:
            console.print(
                "[bold yellow]No data found for the specified range.[/bold yellow]"
            )
            return

        history_table = Table(title="Historical Environmental Data", style="cyan")
        # Dynamically add columns based on the keys of the first data entry
        for key in data[0].keys():
            history_table.add_column(key.replace("_", " ").title(), style="bold")

        for row_data in data:
            history_table.add_row(*[str(value) for value in row_data.values()])

        console.print(history_table)

    except ValueError:
        console.print(
            "[bold red]Invalid date format. Please use YYYY-MM-DD.[/bold red]"
        )
    except Exception as e:
        console.print(f"[bold red]An error occurred: {e}[/bold red]")