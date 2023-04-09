from time import sleep
from data.showtime import Showtime
from databaseSDK import showtimes

# installation: pyinstaller --specpath build --clean --onefile main.py

for i in range(3):
    showtimes.add(Showtime(42, "twilight", "1.02.2023", "18:23"))
    # showtimes.remove(showtimes.find_by_name("twilight")[0])


for item in showtimes.get_all():
    print(" ".join([str(item.id), item.movie_name, item.date, item.time]))

sleep(3)
