
# Environmental Monitoring System CLI

This is a simple, command-line interface (CLI) application built with Python to monitor environmental data like air quality and weather conditions. It fetches real-time data from public APIs, stores it in a local SQLite database, and alerts the user if readings exceed pre-configured safety thresholds.

## Features

- **Fetch Real-time Data**: Get current weather and air quality information from OpenWeatherMap and AirVisual.
- **Local Data Persistence**: Store historical data in an SQLite database.
- **Customizable Thresholds**: Set your own safety limits for various environmental metrics.
- **Alerting System**: Receive alerts when any metric exceeds its safety threshold.
- **Historical Data Query**: View past readings over a specified date range.
- **Health & Safety Tips**: Get simple, actionable advice based on current conditions.

## Team Members

- Victor Hamzat
- Liata Ornella
- Victor Idowu
- Aiyedogbon Ayobamidele
- Jean Luc Mucyo Ndahimana

## Project Structure

```
.environmental-monitoring-system/
├── .env
├── .env.example
├── .gitignore
├── README.md
├── api_handler.py
├── alerter.py
├── cli.py
├── config.py
├── db_handler.py
├── environmental_data.db
├── main.py
├── requirements.txt
└── tips.py
```

## Getting Started

### Prerequisites

- Python 3.6+
- `pip` for installing packages

### Installation

1. **Clone the repository (or download the files):**

    ```bash
    git clone <repository_url>
    cd environmental-monitoring-system
    ```

2. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your API keys:**
    - Rename the `.env.example` file to `.env`.
    - Open the `.env` file and add your API keys from [OpenWeatherMap](https://openweathermap.org/api) and [AirVisual](https://www.iqair.com/commercial/air-quality-monitors/airvisual-platform/api).

    ```
    OPENWEATHER_API_KEY="your_openweathermap_api_key"
    AIRVISUAL_API_KEY="your_airvisual_api_key"
    ```

    *Note: The application can run without API keys, but it will use placeholder data.*

### Running the Application

To start the CLI, run the `main.py` script:

```bash
python3 main.py
```

You will be greeted with the main menu:

```
–––––––––––––––––––––––––––––––––––––––––––––
  ENVIRONMENTAL MONITORING – CLI v1.0
–––––––––––––––––––––––––––––––––––––––––––––

[1] Fetch & Log Current Data
[2] Show Latest Readings
[3] Query Historical Data
[4] Set Safety Thresholds
[5] View Health & Safety Tips
[6] Exit
–––––––––––––––––––––––––––––––––––––––––––––
Choose (1–6):
```

## How It Works

- **`main.py`**: The entry point of the application. It initializes the database and runs the main CLI loop.
- **`cli.py`**: Handles all user interaction, including displaying menus and processing user input.
- **`api_handler.py`**: Manages requests to the external weather and air quality APIs.
- **`db_handler.py`**: Contains all functions for interacting with the SQLite database (CRUD operations).
- **`alerter.py`**: Checks the latest data against the user-defined or default thresholds.
- **`config.py`**: Stores the default safety thresholds.
- **`tips.py`**: Provides health advice based on the current environmental alerts.

## Future Improvements

- Add support for more data sources and metrics.
- Implement more sophisticated data visualization (e.g., ASCII charts).
- Add unit tests for better reliability.
- Package the application for easier distribution.
