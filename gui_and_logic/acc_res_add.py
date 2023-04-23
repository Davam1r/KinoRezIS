from tkinter import Tk, messagebox, LabelFrame, Label, Entry, Button,\
                    StringVar
from tkinter.ttk import Treeview, Style
from typing import Tuple, List
from databaseSDK import reservations, showtimes
from data import Reservation, Showtime
from constants import BASEFONT, BUTTONFONT

__showtimes: List[Showtime]


def __extract_values(mov: Showtime) -> Tuple[str, str, str]:
    return (mov.movie_name, mov.date, mov.time)


def __click_load_data(table: Treeview, movie: StringVar,
                      date: StringVar, time: StringVar) -> None:
    selected = table.focus()
    if selected == "":
        return

    item = table.item(selected)

    movie.set(item["values"][0])
    date.set(item["values"][1])
    time.set(item["values"][2])


def __search(table: Treeview, name: str) -> None:
    table.delete(*table.get_children())
    global __showtimes
    __showtimes = (showtimes.find_by_name(name))
    for mov in __showtimes:
        table.insert('', 'end', values=__extract_values(mov))


def __add_reservation(table: Treeview, name: str) -> None:
    selected = table.focus()
    if name == "":
        messagebox.showerror('', "Nevyplněno jméno zákazníka.")
        return
    if selected == "":
        messagebox.showerror('',
                             "Nebyl vybrán promítací termín k rezervaci.\n\n" +
                             "Proveďte výběr kliknutím na řádek v tabulce,\n"
                             + "data z řádku se zobrazí ve spodní části okna.")
        return

    showtimeID = __showtimes[table.index(selected)].id
    res = Reservation(name, Showtime("", "", "", showtimeID))
    reservations.add(res)
    messagebox.showinfo('', "Rezervace byla přidána")


def __load_showtimes(table: Treeview) -> None:
    global __showtimes
    __showtimes = showtimes.get_all()
    for mov in __showtimes:
        table.insert('', 'end', values=__extract_values(mov))


def __movie_table(frame: LabelFrame) -> Treeview:
    style = Style()
    style.theme_use("clam")
    style.configure("myS.Treeview", font=BASEFONT)
    style.configure("myS.Treeview.Heading", font=("Arial", 14, "bold"))

    table = Treeview(frame, columns=("1", "2", "3"), style="myS.Treeview",
                     show="headings", height=10)

    table.heading(1, text="Film")
    table.heading(2, text="Datum")
    table.heading(3, text="Čas")

    table.column(1, anchor="center", width=400, stretch=False)
    table.column(2, anchor="center", width=100)
    table.column(3, anchor="center", width=30)

    table.pack(fill="both", padx=10, pady=5)

    __load_showtimes(table)

    return table


def __movie_namesearch(frame: LabelFrame, table: Treeview) -> None:
    label1 = Label(frame, text="Vyhledávání dle filmu:", font=BASEFONT)
    label1.pack(side="left", padx=20)
    entry = Entry(frame, font=BASEFONT)
    entry.pack(side="left", padx=10)
    search_btn = Button(frame, text="Vyhledat", font=BUTTONFONT,
                        command=lambda: __search(
                                        table, entry.get().strip()))
    search_btn.pack(side="left", padx=20)


def __res_add(frame: LabelFrame, table: Treeview) -> None:
    movie, date, name = StringVar(), StringVar(), StringVar()
    time = StringVar()

    name_l = Label(frame, text="Jméno:", font=BASEFONT)
    name_l.grid(row=0, column=0, padx=20, pady=10)
    name_e = Entry(frame, textvariable=name, font=BASEFONT)
    name_e.grid(row=0, column=1)

    movie_l = Label(frame, text="Film:", font=BASEFONT)
    movie_l.grid(row=1, column=0, padx=20, pady=10)
    movie_e = Entry(frame, textvariable=movie, font=BASEFONT)
    movie_e.grid(row=1, column=1)

    date_l = Label(frame, text="Datum:", font=BASEFONT)
    date_l.grid(row=2, column=0, padx=20, pady=10)
    date_e = Entry(frame, textvariable=date, font=BASEFONT)
    date_e.grid(row=2, column=1)

    time_l = Label(frame, text="Čas:", font=BASEFONT)
    time_l.grid(row=3, column=0, padx=20, pady=10)
    time_e = Entry(frame, textvariable=time, font=BASEFONT)
    time_e.grid(row=3, column=1)

    delete_btn = Button(frame, text="Zapsat rezervaci", font=BUTTONFONT,
                        command=lambda: __add_reservation(
                                        table, name.get()))
    delete_btn.grid(row=1, column=2, padx=40)

    # click item to preload data in entries
    table.bind("<<TreeviewSelect>>",
               lambda _: __click_load_data(table, movie, date, time))


def add_reservations() -> None:
    """
    Opens Reservation management screen
    """
    root = Tk()
    root.title("KinoRezIS")
    root.geometry("800x650+300+200")

    frame1 = LabelFrame(root, text="Seznam promítacích termínů")
    frame2 = LabelFrame(root, text="Vyhledávání")
    frame3 = LabelFrame(root, text="Přidání rezervace")
    for f in frame1, frame2, frame3:
        f.pack(fill="both", expand=1, padx=10, pady=10)

    table = __movie_table(frame1)

    __movie_namesearch(frame2, table)

    __res_add(frame3, table)

    root.mainloop()
