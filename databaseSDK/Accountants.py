from typing import List
from data.accountant import Accountant
from databaseSDK._db_cursor import get_cursor as __get_cursor


__cursor = __get_cursor()


__cursor.execute('''CREATE TABLE IF NOT EXISTS accountants
                  (name TEXT, login TEXT, password TEXT)''')
__cursor.connection.commit()


def add(accountant: Accountant) -> None:
    if (accountant.name is None or accountant.login is None or
            accountant.password is None):
        return

    __cursor.execute("INSERT INTO accountants VALUES (?, ?, ?)",
                     (accountant.name, accountant.login, accountant.password))
    __cursor.connection.commit()


def remove(accountant: Accountant) -> None:
    __cursor.execute("DELETE FROM accountants WHERE \
                     name=? AND login=? AND password=?",
                     (accountant.name, accountant.login, accountant.password))
    __cursor.connection.commit()


def find_by_name(inp_name: str) -> List[Accountant]:
    __cursor.execute("SELECT * FROM accountants \
                   WHERE name=?", (inp_name,))

    accountants: List[Accountant] = []
    for name, login, password in __cursor.fetchall():
        accountants.append(Accountant(name, login, password))

    return accountants


def get_all() -> List[Accountant]:
    accountants: List[Accountant] = []

    for name, login, password in __cursor.execute("SELECT * FROM accountants"):
        accountants.append(Accountant(name, login, password))

    return accountants
