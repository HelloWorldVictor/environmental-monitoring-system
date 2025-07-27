import sqlite3

DB_NAME = "environmental_data.db"


def initialize_db():
    """Initializes the database and creates tables if they don't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create data table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            temperature REAL,
            humidity REAL,
            co2 REAL,
            co REAL,
            pm25 REAL,
            pm10 REAL
        )
    """
    )

    # Create thresholds table
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS thresholds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            metric TEXT UNIQUE,
            min_val REAL,
            max_val REAL
        )
    """
    )
    conn.commit()
    conn.close()

def save_data(data):
    """Saves a new data reading to the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO readings (temperature, humidity, co2, co, pm25, pm10)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data.get("temperature"),
        data.get("humidity"),
        data.get("co2"),
        data.get("co"),
        data.get("pm25"),
        data.get("pm10")
    ))
    conn.commit()
    conn.close()

def get_latest_readings():
    """Retrieves the most recent data reading."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM readings ORDER BY timestamp DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if row:
        # Return as a dictionary
        keys = [description[0] for description in cursor.description]
        return dict(zip(keys, row))
    return None

def get_historical_data(start_date, end_date):
    """Retrieves data within a specified date range."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM readings WHERE timestamp BETWEEN ? AND ?",
        (start_date, end_date)
    )
    rows = cursor.fetchall()
    conn.close()
    # Return as a list of dictionaries
    keys = [description[0] for description in cursor.description]
    return [dict(zip(keys, row)) for row in rows]
