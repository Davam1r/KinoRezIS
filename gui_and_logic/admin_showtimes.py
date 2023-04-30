from datetime import datetime
from tkinter import END, Button, Entry, Frame, Label, Tk, messagebox

from constants import BASEFONT, BUTTONFONT
from data import Showtime
from databaseSDK import showtimes


def __date_valid(date: str) -> bool:
    segments = date.split(".")
    if len(segments) != 3:
        return False

    try:
        day, month, year = int(segments[0]), int(segments[1]), int(segments[2])
    except Exception:
        return False

    cur_year = datetime.now().year
    if not (0 <= day <= 31 and 0 <= month <= 12 and
            cur_year <= year <= cur_year+1):
        return False
    return True


def __time_valid(time: str) -> bool:
    segments = time.split(":")
    if len(segments) != 2:
        return False

    try:
        hour, minute = int(segments[0]), int(segments[1])
    except Exception:
        return False

    if not (0 <= hour <= 23 and 0 <= minute <= 59):
        return False
    return True


def __check_showtime_format(showtime: Showtime) -> bool:
    if showtime.movie_name == "" or showtime.date == "" or showtime.time == "":
        return False
    if not __date_valid(showtime.date):
        return False
    if not __time_valid(showtime.time):
        return False
    return True


def __add_showtime_to_db(showtime: Showtime, entries: list[Entry]) -> None:
    if not __check_showtime_format(showtime):
        messagebox.showerror("error",
                             "Termín nesplňuje formát nebo je" +
                             "příliš vzdálený současnosti.\n\n" +
                             "Formát data:  DEN.MESIC.ROK\n" +
                             "Formát času:  HODINA:MINUT")
        return

    showtimes.add(showtime)
    messagebox.showinfo("", "Promítací termín úspěšně přidán")

    for entry in entries:
        entry.delete(0, END)


def add_showtime() -> None:
    """
    Opens screen with option to add new showtimes
    """
    root = Tk()
    root.title("KinoRezIS")
    root.geometry("400x300+400+300")

    frame = Frame()
    frame.pack(pady=20)

    label1 = Label(frame, text="Název filmu: ", font=BASEFONT)
    label1.grid(row=0, column=0)
    label2 = Label(frame, text="Datum: ", font=BASEFONT)
    label2.grid(row=1, column=0)
    label3 = Label(frame, text="Čas: ", font=BASEFONT)
    label3.grid(row=2, column=0)

    name_entry = Entry(frame, font=BASEFONT)
    name_entry.grid(row=0, column=1, pady=20)
    date_entry = Entry(frame, font=BASEFONT)
    date_entry.insert(0, "DEN.MESIC.ROK")
    date_entry.grid(row=1, column=1)
    time_entry = Entry(frame, font=BASEFONT)
    time_entry.insert(0, "HODINA:MINUTA")
    time_entry.grid(row=2, column=1, pady=20)

    entries = [name_entry, date_entry, time_entry]

    button = Button(frame, text="Přidat promítací termín", font=BUTTONFONT,
                    command=lambda: __add_showtime_to_db(
                                    Showtime(name_entry.get().strip(),
                                             date_entry.get().strip(),
                                             time_entry.get().strip()),
                                    entries))
    button.grid(row=3, pady=20, columnspan=2)
    root.bind("<Return>",  # enter key can act as button press too
              lambda _: __add_showtime_to_db(
                        Showtime(name_entry.get().strip(),
                                 date_entry.get().strip(),
                                 time_entry.get().strip()),
                        entries))

    root.mainloop()
