import sqlite3
from typing import List
from data.accountant import Accountant


cursor = sqlite3.connect("users.db").cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS accountants
                  (name TEXT, login TEXT, password TEXT)''')
cursor.connection.commit()


def add(reservation: Accountant) -> None:
    pass


def remove(reservation: Accountant) -> None:
    pass


def find(reservation: Accountant) -> None:
    pass


def get_all() -> List[Accountant]:
    pass
