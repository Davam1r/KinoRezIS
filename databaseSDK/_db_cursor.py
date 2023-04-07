import sqlite3


DB_NAME = "users.db"


def get_cursor() -> sqlite3.Cursor:
    return sqlite3.connect(DB_NAME).cursor()
