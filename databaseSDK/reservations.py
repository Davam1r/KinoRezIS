from typing import List

from data import Reservation, Showtime
from databaseSDK._db_cursor import cursor as __cursor

__cursor.execute('''CREATE TABLE IF NOT EXISTS reservations
                  (name TEXT, showtimeID INTEGER)''')
__cursor.connection.commit()


def add(reservation: Reservation) -> None:
    """
    Adds a reservation to database

    @param reservation
    """
    if (reservation.name is None or reservation.showtime is None):
        return

    __cursor.execute("INSERT INTO reservations VALUES (?, ?)",
                     (reservation.name, reservation.showtime.id))
    __cursor.connection.commit()


def remove(res: Reservation) -> None:
    """
    Removes a reservation from database

    @param reservation
    """
    __cursor.execute("DELETE FROM reservations WHERE rowid IN \
                     (SELECT showtimeID FROM reservations JOIN showtimes ON \
                     reservations.showtimeID=showtimes.rowid WHERE \
                     reservations.name=? AND showtimes.name=? AND \
                     showtimes.date=? AND showtimes.time=? LIMIT 1)",
                     (res.name, res.showtime.movie_name,
                      res.showtime.date, res.showtime.time))
    __cursor.connection.commit()


def __remove_expired() -> None:
    __cursor.execute("DELETE FROM reservations WHERE showtimeID NOT IN \
                     (SELECT rowid FROM showtimes)")
    __cursor.connection.commit()


def find_by_name(inp_name: str) -> List[Reservation]:
    """
    @param inp_name reservation customer name

    @return list of reservations with inp_name
    """
    __remove_expired()

    __cursor.execute("SELECT reservations.name, \
                      showtimes.name, showtimes.date, showtimes.time \
                      FROM reservations JOIN showtimes ON \
                      reservations.showtimeID=showtimes.rowid \
        WHERE reservations.name LIKE ? COLLATE NOCASE", ('%'+inp_name+'%',))

    reservations: List[Reservation] = []
    for name, movie_name, date, time in __cursor.fetchall():
        showtime = Showtime(movie_name, date, time)
        reservations.append(Reservation(name, showtime))

    return reservations


def get_all() -> List[Reservation]:
    """
    @return list of all reservations
    """
    __remove_expired()

    __cursor.execute("SELECT reservations.name, \
                      showtimes.name, showtimes.date, showtimes.time \
                      FROM reservations JOIN showtimes ON \
                      reservations.showtimeID=showtimes.rowid")

    reservations: List[Reservation] = []
    for name, movie_name, date, time in __cursor.fetchall():
        showtime = Showtime(movie_name, date, time)
        reservations.append(Reservation(name, showtime))

    return reservations
