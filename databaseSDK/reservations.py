from typing import List
from data.reservation import Reservation
from databaseSDK._db_cursor import cursor as __cursor


__cursor.execute('''CREATE TABLE IF NOT EXISTS reservations
                  (name TEXT, showtimeID INTEGER)''')
__cursor.connection.commit()


def add(reservation: Reservation) -> None:
    if (reservation.name is None or reservation.showtime is None):
        return

    __cursor.execute("INSERT INTO reservations VALUES (?, ?)",
                     (reservation.name, reservation.showtime.id))
    __cursor.connection.commit()


def remove(reservation: Reservation) -> None:
    __cursor.execute("DELETE FROM reservations WHERE \
                    name=? AND showtimeID=?",
                     (reservation.name, reservation.showtime.id))
    __cursor.connection.commit()


def find_by_name(inp_name: str) -> List[Reservation]:
    __cursor.execute("SELECT * FROM reservations \
                   WHERE name=?", (inp_name,))

    reservations: List[Reservation] = []
    for name, showtimeID in __cursor.fetchall():
        reservations.append(Reservation(name, showtimeID))

    return reservations


def get_all() -> List[Reservation]:
    reservations: List[Reservation] = []

    for name, showtimeID in __cursor.execute("SELECT * FROM reservations"):
        reservations.append(Reservation(name, showtimeID))

    return reservations
