import sqlite3

DATABASE = "database.db"


def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS warranty_period (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            facebook TEXT,
            phone_number INTEGER,
            expired_date INTEGER
        )
        """
    )

    conn.close()


def add_warranty(user_info):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO warranty_period
            (name, facebook, phone_number, expired_date)
        values
            (?, ?, ?, ?)
        """,
        (
            user_info["name"],
            user_info["facebook"],
            user_info["phone_number"],
            user_info["expired_date"],
        ),
    )

    conn.commit()
    conn.close()


def get_all_warranties():
    conn = sqlite3.connect(DATABASE)
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
