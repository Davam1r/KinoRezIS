from typing import List
from data import Reservation
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


def remove(reservation: Reservation) -> None:
    """
    Removes a reservation from database

    @param reservation
    """
    __cursor.execute("DELETE FROM reservations WHERE \
                    name=? AND showtimeID=?",
                     (reservation.name, reservation.showtime.id))
    __cursor.connection.commit()


def find_by_name(inp_name: str) -> List[Reservation]:
    """
    @param inp_name reservation customer name

    @return list of reservations with inp_name
    """
    __cursor.execute("SELECT * FROM reservations \
                WHERE name LIKE ? COLLATE NOCASE", ('%'+inp_name+'%',))

    reservations: List[Reservation] = []
    for name, showtimeID in __cursor.fetchall():
        reservations.append(Reservation(name, showtimeID))

    return reservations


def get_all() -> List[Reservation]:
    """
    @return list of all reservations
    """
    reservations: List[Reservation] = []

    for name, showtimeID in __cursor.execute("SELECT * FROM reservations"):
        reservations.append(Reservation(name, showtimeID))

    return reservations
