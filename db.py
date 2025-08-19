import sqlite3

def create_tables():
    with sqlite3.connect("database/users.db") as db:
        cursor = db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER UNIQUE,
                first_name TEXT,
                phone TEXT,
                registered_at TEXT
            )
        """)
        db.commit()

def add_user(telegram_id, first_name, phone, registered_at):
    with sqlite3.connect("database/users.db") as db:
        cursor = db.cursor()
        cursor.execute("""
            INSERT OR IGNORE INTO users (telegram_id, first_name, phone, registered_at)
            VALUES (?, ?, ?, ?)
        """, (telegram_id, first_name, phone, registered_at))
        db.commit()
