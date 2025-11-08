import sqlite3

DATABASE_PATH = "database.db"


def create_database():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS warranty_period (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            facebook TEXT,
            phone_number INTEGER,
            expired_date INTEGER,
            note TEXT
        ) """
    )

    conn.close()


def add_warranty(new_warranty):
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO warranty_period
            (name, facebook, phone_number, expired_date, note)
        values
            (?, ?, ?, ?, ?)
        """,
        (
            new_warranty["name"],
            new_warranty["facebook"],
            new_warranty["phone_number"],
            new_warranty["expired_date"],
            new_warranty["note"],
        ),
    )

    conn.commit()
    conn.close()


def get_all_warranties():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM warranty_period
        """
    )

    result = [dict(i) for i in cursor.fetchall()]
    conn.close()

    return result
