import sqlite3
from typing import List
from data.reservation import Reservation


cursor = sqlite3.connect("users.db").cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS reservations
                  (name TEXT, showtimeID INTEGER)''')
cursor.connection.commit()


def add(reservation: Reservation) -> None:
    pass


def remove(reservation: Reservation) -> None:
    pass


def find(reservation: Reservation) -> None:
    pass


def get_all() -> List[Reservation]:
    pass
