from data.showtime import Showtime
from databaseSDK import showtimes


showtimes.add(Showtime(42, "twilight", "1.02.2023", "18:23"))

for item in showtimes.get_all():
    print(item.id)
    print(item.movie_name + item.date + item.time)
