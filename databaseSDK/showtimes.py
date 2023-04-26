from typing import List
from data import Showtime
from databaseSDK._db_cursor import cursor as __cursor
from datetime import datetime


__cursor.execute('''CREATE TABLE IF NOT EXISTS showtimes
                  (name TEXT, date TEXT, time TEXT)''')
__cursor.connection.commit()


def add(showtime: Showtime) -> None:
    """
    Adds a showtime to database

    @param showtime
    """
    if (showtime.movie_name is None or
            showtime.date is None or showtime.time is None):
        return

    __cursor.execute("INSERT INTO showtimes VALUES (?, ?, ?)",
                     (showtime.movie_name,
                      showtime.date, showtime.time))
    __cursor.connection.commit()


def remove(showtime: Showtime) -> None:
    """
    Removes a showtime from database

    @param showtime
    """
    __cursor.execute("DELETE FROM showtimes WHERE \
                     rowid=?", (showtime.id, ))
    __cursor.connection.commit()


def __date_expired(showtime_date: str) -> bool:
    cur_datetime = datetime.now()

    segments = showtime_date.split(".")
    day, month, year = int(segments[0]), int(segments[1]), int(segments[2])
    showtime_datetime = datetime(year, month, day)

    return showtime_datetime < cur_datetime


def __remove_expired() -> None:
    """
    Remove showtimes with date that is in the past
    """
    __cursor.execute("SELECT rowid, date FROM showtimes")

    for rowid, date in __cursor.fetchall():
        if __date_expired(date):
            __cursor.execute("DELETE FROM showtimes WHERE \
                             rowid=?", (rowid, ))
    __cursor.connection.commit()


def find_by_name(inp_name: str) -> List[Showtime]:
    """
    @param inp_name movie name

    @return list of showtimes for certain movie name
    """
    __remove_expired()

    __cursor.execute("SELECT rowid, name, date, time FROM showtimes \
                WHERE name LIKE ? COLLATE NOCASE", ('%'+inp_name+'%',))

    showtimes: List[Showtime] = []
    for id, name, date, time in __cursor.fetchall():
        showtimes.append(Showtime(name, date, time, id))

    return showtimes


def get_all() -> List[Showtime]:
    """
    @return list of all showtimes
    """
    __remove_expired()

    showtimes: List[Showtime] = []
    for id, name, date, time in __cursor.execute(
            "SELECT rowid, name, date, time FROM showtimes"):
        showtimes.append(Showtime(name, date, time, id))

    return showtimes
