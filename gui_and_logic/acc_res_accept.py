from tkinter import Button, Entry, Label, LabelFrame, StringVar, Tk, messagebox
from tkinter.ttk import Style, Treeview
from typing import Tuple

from constants import BASEFONT, BUTTONFONT
from data import Reservation, Showtime
from databaseSDK import reservations


def __extract_values(res: Reservation) -> Tuple[str, str, str, str]:
    """
    Extracts values out of Reservation to a tuple that represents
    one record in the table of Reservations

    @param res Reservation

    @return tuple that represents one record in table of Reservations
    """
    return (res.name, res.showtime.movie_name,
            res.showtime.date, res.showtime.time)


def __click_load_data(table: Treeview,
                      name: StringVar, movie: StringVar,
                      date: StringVar, time: StringVar) -> None:
    """
    Loads data from clicked record in the table into correct GUI entries

    @param table
    @param name
    @param movie
    @param date
    @param time
    """
    selected = table.focus()
    if selected == "":
        return

    item = table.item(selected)

    name.set(item["values"][0])
    movie.set(item["values"][1])
    date.set(item["values"][2])
    time.set(item["values"][3])


def __search(table: Treeview, name: str) -> None:
    """
    Loads records that have 'name' as a substring from database
    into Treeview table

    @param table
    @param name substring to be searched in reservations DB
    """
    table.delete(*table.get_children())
    for res in reservations.find_by_name(name):
        table.insert('', 'end', values=__extract_values(res))


def __remove_reservation(table: Treeview) -> None:
    """
    Removes Reservation selected in Treeview table from
    both the table and reservation DB

    @param table
    """
    selected = table.focus()
    if selected == "":
        messagebox.showerror('',
                             "Rezervace k potvrzení nebyla vybrána\n\n" +
                             "Proveďte výběr kliknutím na řádek v tabulce,\n"
                             + "data z řádku se zobrazí ve spodní části okna.")
        return

    selected_item = table.item(selected)
    name = selected_item["values"][0]
    movie = selected_item["values"][1]
    date = selected_item["values"][2]
    time = selected_item["values"][3]
    res = Reservation(name, Showtime(movie, date, time))

    reservations.remove(res)
    table.delete(selected)
    messagebox.showinfo('', "Využití rezervace bylo potvrzeno")


def __load_reservations(table: Treeview) -> None:
    """
    Load reservations from database into specified Treeview table

    @param table
    """
    for res in reservations.get_all():
        table.insert('', 'end', values=__extract_values(res))


def __table(frame: LabelFrame) -> Treeview:
    """
    Draws a Treeview table for showing reservations
    into specified GUI frame

    @param frame

    @return created Treeview table
    """
    style = Style()
    style.theme_use("clam")
    style.configure("myS.Treeview", font=BASEFONT)
    style.configure("myS.Treeview.Heading", font=("Arial", 14, "bold"))

    table = Treeview(frame, columns=("1", "2", "3", "4"), style="myS.Treeview",
                     show="headings", height=10)
    table.pack(fill="both", padx=10, pady=5)

    table.heading(1, text="Jméno")
    table.heading(2, text="Film")
    table.heading(3, text="Datum")
    table.heading(4, text="Čas")

    table.column(1, anchor="center", width=220, stretch=False)
    table.column(2, anchor="center", width=320, stretch=False)
    table.column(3, anchor="center", width=100)
    table.column(4, anchor="center", width=30)

    return table


def __namesearch(frame: LabelFrame, table: Treeview) -> None:
    """
    Draws namesearch section elements into specified GUI frame
    These elements are: search Entry, search Button

    @param frame
    @param table needed for button action
    """
    label1 = Label(frame, text="Vyhledávání dle jména:", font=BASEFONT)
    label1.pack(side="left", padx=20)
    entry = Entry(frame, font=BASEFONT)
    entry.pack(side="left", padx=10)
    search_btn = Button(frame, text="Vyhledat", font=BUTTONFONT,
                        command=lambda: __search(
                                        table, entry.get().strip()))
    search_btn.pack(side="left", padx=20)


def __res_accept(frame: LabelFrame, table: Treeview) -> None:
    """
    Draws reservation acceptation elements into specified GUI frame
    These elements are:
    Entries for data from selected record in Treeview
    Accept button

    Includes functionality for loading data by clicking a record

    @param frame
    @param table needed for button action and data loading
    """
    name, movie, date = StringVar(), StringVar(), StringVar()
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

    delete_btn = Button(frame, text="Potvrdit využití rezervace",
                        font=BUTTONFONT,
                        command=lambda: __remove_reservation(table))
    delete_btn.grid(row=1, column=2, padx=60)

    # click item to preload data in entries
    table.bind("<<TreeviewSelect>>", lambda _: __click_load_data(
                table, name, movie, date, time))


def accept_reservations() -> None:
    """
    Draws Reservation management screen
    """
    root = Tk()
    root.title("KinoRezIS")
    root.geometry("800x650+300+200")

    frame1 = LabelFrame(root, text="Seznam rezervací")
    frame2 = LabelFrame(root, text="Vyhledávání")
    frame3 = LabelFrame(root, text="Potvrzení využití rezervace")
    for f in frame1, frame2, frame3:
        f.pack(fill="both", expand=1, padx=10, pady=10)

    table = __table(frame1)
    __load_reservations(table)

    __namesearch(frame2, table)

    __res_accept(frame3, table)

    root.mainloop()
