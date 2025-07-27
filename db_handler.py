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
