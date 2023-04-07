import sqlite3
from typing import List
from data.showtime import Showtime


cursor = sqlite3.connect("users.db").cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS accountants
                  (name TEXT, login TEXT, password TEXT)''')
cursor.connection.commit()


def add(reservation: Showtime) -> None:
    pass


def remove(reservation: Showtime) -> None:
    pass


def find(reservation: Showtime) -> None:
    pass


def get_all() -> List[Showtime]:
    pass
