from typing import List
from data.showtime import Showtime
from databaseSDK._db_cursor import get_cursor as __get_cursor


__cursor = __get_cursor()


__cursor.execute('''CREATE TABLE IF NOT EXISTS showtimes
                  (ID INTEGER, name TEXT, date TEXT, time TEXT)''')
__cursor.connection.commit()

__showtime_cnt = __cursor.execute("SELECT MAX(ID)\
                                FROM showtimes").fetchone()[0]
if __showtime_cnt is None:
    __showtime_cnt = 0


def add(showtime: Showtime) -> None:
    global __showtime_cnt
    __showtime_cnt += 1
    if (showtime.id is None or showtime.movie_name is None or
            showtime.date is None or showtime.id is None):
        return

    __cursor.execute("INSERT INTO showtimes VALUES (?, ?, ?, ?)",
                     (__showtime_cnt, showtime.movie_name,
                      showtime.date, showtime.time))
    __cursor.connection.commit()


def remove(showtime: Showtime) -> None:
    __cursor.execute("DELETE FROM showtimes WHERE \
                   ID=?", (showtime.id, ))
    __cursor.connection.commit()


def find_by_name(inp_name: str) -> List[Showtime]:
    __cursor.execute("SELECT * FROM showtimes \
                   WHERE name=?", (inp_name,))

    showtimes: List[Showtime] = []
    for id, name, date, time in __cursor.fetchall():
        showtimes.append(Showtime(id, name, date, time))

    return showtimes


def get_all() -> List[Showtime]:
    showtimes: List[Showtime] = []

    for id, name, date, time in __cursor.execute("SELECT * FROM showtimes"):
        showtimes.append(Showtime(id, name, date, time))

    return showtimes
