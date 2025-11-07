import os
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


def print_help():
    print(
        "help    show help messages\n"
        "exit    exit the program\n"
        "add     add a new warranty\n"
        "list    list all the warranties"
    )


def main():
    print_help()

    if not os.path.exists(DATABASE):
        create_database()

    while True:
        command = input(">: ")

        if command == "exit":
            exit()

        elif command == "help":
            print_help()

        elif command == "add":
            user_info = {
                "name": input("name: "),
                "facebook": input("facebook: "),
                "phone_number": input("phone_number: "),
                "expired_date": input("expired_date: "),
            }
            add_warranty(user_info)

        elif command == "list":
            all_warranties = get_all_warranties()
            [print(i) for i in all_warranties]


if __name__ == "__main__":
    main()
