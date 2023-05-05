from typing import List

from data import Accountant
from databaseSDK._db_cursor import cursor as __cursor

__cursor.execute('''CREATE TABLE IF NOT EXISTS accountants
                  (name TEXT, login TEXT, password TEXT)''')
__cursor.connection.commit()


def add(accountant: Accountant) -> None:
    """
    Adds an accountant to database

    @param accountant
    """
    if (accountant is None or accountant.name is None or
            accountant.login is None or accountant.password is None):
        return

    __cursor.execute("INSERT INTO accountants VALUES (?, ?, ?)",
                     (accountant.name, accountant.login, accountant.password))
    __cursor.connection.commit()


def remove(accountant: Accountant) -> None:
    """
    Removes an accountant from database

    @param accountant
    """
    __cursor.execute("DELETE FROM accountants WHERE \
                     name=? AND login=? AND password=?",
                     (accountant.name, accountant.login, accountant.password))
    __cursor.connection.commit()


def find_by_name(inp_name: str) -> List[Accountant]:
    """
    @param inp_name accountant name

    @return list of accountants with inp_name
    """
    __cursor.execute("SELECT * FROM accountants \
                WHERE name LIKE ? COLLATE NOCASE", ('%'+inp_name+'%',))

    accountants: List[Accountant] = []
    for name, login, password in __cursor.fetchall():
        accountants.append(Accountant(name, login, password))

    return accountants


def accountant_login_exists(inp_login: str, inp_password: str) -> bool:
    """
    @param  inp_login
    @param  inp_password

    @return false if accountant with inp_login and inp_name was not found
            otherwise true
    """
    __cursor.execute("SELECT * FROM accountants \
                   WHERE login=? AND password=?", (inp_login, inp_password))

    entry = __cursor.fetchone()

    return entry is not None


def get_all() -> List[Accountant]:
    """
    @return list of all accountants
    """
    accountants: List[Accountant] = []

    for name, login, password in __cursor.execute("SELECT * FROM accountants"):
        accountants.append(Accountant(name, login, password))

    return accountants
