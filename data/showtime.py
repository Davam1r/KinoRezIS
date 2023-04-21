from typing import Optional


class Showtime:
    def __init__(self, movie_name: str, date: str, time: str,
                 id: Optional[int] = None) -> None:
        self.id = id
        self.movie_name = movie_name
        self.date = date
        self.time = time
