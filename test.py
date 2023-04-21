from databaseSDK import showtimes

for showtime in showtimes.get_all():
    print(showtime.movie_name + " | " +
          showtime.date + " | " +
          showtime.time)
