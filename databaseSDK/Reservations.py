import sqlite3
from data import Reservation


cursor = sqlite3.connect("users.db").cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS reservations
                  (name TEXT, showtimeID INTEGER)''')


def add(reservation: Reservation) -> None:
    pass
