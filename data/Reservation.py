from data.showtime import Showtime


class Reservation:
    def __init__(self, name: str, showtime: Showtime) -> None:
        self.name = name
        self.showtime = showtime
