import sqlite3

DB_NAME = ".data.db"


cursor = sqlite3.connect(DB_NAME).cursor()
