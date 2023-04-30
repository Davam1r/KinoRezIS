from tkinter import Button, Entry, Label, LabelFrame, StringVar, Tk, messagebox
from tkinter.ttk import Style, Treeview

from constants import BASEFONT, BUTTONFONT
from data import Accountant
from databaseSDK import accountants


def __click_load_data(table: Treeview,
                      name: StringVar, login: StringVar,
                      passwd: StringVar) -> None:
    selected = table.focus()
    if selected == "":
        return

    item = table.item(selected)

    name.set(item["values"][0])
    login.set(item["values"][1])
    passwd.set(item["values"][2])


def __search(table: Treeview, name: str) -> None:
    table.delete(*table.get_children())
    for acc in accountants.find_by_name(name):
        table.insert('', 'end', values=(acc.name, acc.login, acc.password))


def __add_accountant(acc: Accountant, table: Treeview) -> None:
    if "" in [acc.login, acc.name, acc.password]:
        messagebox.showerror('', "Informace o účetním nejsou vyplněny.")
        return
    accountants.add(acc)
    table.insert('', 0, values=(acc.name, acc.login, acc.password))
    messagebox.showinfo('', "Účetní byl úspěšně přidán")


def __remove_accountant(table: Treeview) -> None:
    selected = table.focus()
    if selected == "":
        messagebox.showerror('',
                             "Účetní ke smazání nebyl vybrán\n\n" +
                             "Proveďte výběr kliknutím na řádek v tabulce,\n"
                             + "data z řádku se zobrazí ve spodní části okna.")
        return

    selected_item = table.item(selected)
    name = selected_item["values"][0]
    login = selected_item["values"][1]
    passwd = selected_item["values"][2]

    accountants.remove(Accountant(name, login, passwd))
    table.delete(selected)
    messagebox.showinfo('', "Účetní byl/a úspěšně smazán/a")


def __table(frame: LabelFrame) -> Treeview:
    style = Style()
    style.theme_use("clam")
    style.configure("myS.Treeview", font=BASEFONT)
    style.configure("myS.Treeview.Heading", font=("Arial", 14, "bold"))

    table = Treeview(frame, columns=("1", "2", "3"), style="myS.Treeview",
                     show="headings", height=10)
    table.pack(fill="both", padx=10, pady=5)

    table.heading(1, text="Jméno")
    table.heading(2, text="Login")
    table.heading(3, text="Heslo")

    table.column(1, anchor="center")
    table.column(2, anchor="center")
    table.column(3, anchor="center")

    for acc in accountants.get_all():
        table.insert('', 'end', values=(acc.name, acc.login, acc.password))

    return table


def __namesearch(frame: LabelFrame, table: Treeview) -> None:
    label1 = Label(frame, text="Vyhledávání dle jména:", font=BASEFONT)
    label1.pack(side="left", padx=20)
    entry = Entry(frame, font=BASEFONT)
    entry.pack(side="left", padx=10)
    search_btn = Button(frame, text="Vyhledat", font=BUTTONFONT,
                        command=lambda: __search(table, entry.get().strip()))
    search_btn.pack(side="left", padx=20)


def __management(frame: LabelFrame, table: Treeview) -> None:
    name, login, passwd = StringVar(), StringVar(), StringVar()

    name_l = Label(frame, text="Jméno:", font=BASEFONT)
    name_l.grid(row=0, column=0, padx=20, pady=10)
    name_e = Entry(frame, textvariable=name, font=BASEFONT)
    name_e.grid(row=0, column=1)

    login_l = Label(frame, text="Login:", font=BASEFONT)
    login_l.grid(row=1, column=0, padx=20, pady=10)
    login_e = Entry(frame, textvariable=login, font=BASEFONT)
    login_e.grid(row=1, column=1)

    pass_l = Label(frame, text="Heslo:", font=BASEFONT)
    pass_l.grid(row=2, column=0, padx=20, pady=10)
    pass_e = Entry(frame, textvariable=passwd, font=BASEFONT)
    pass_e.grid(row=2, column=1)

    add_btn = Button(frame, text="Přidat účetní", font=BUTTONFONT,
                     command=lambda: __add_accountant(
                                    Accountant(name.get().strip(),
                                               login.get().strip(),
                                               passwd.get().strip()),
                                    table))
    delete_btn = Button(frame, text="Smazat účetní", font=BUTTONFONT,
                        command=lambda: __remove_accountant(table))
    add_btn.grid(row=1, column=2, padx=40)
    delete_btn.grid(row=1, column=3)

    # click item to preload data in entries
    table.bind("<<TreeviewSelect>>", lambda _: __click_load_data(
                table, name, login, passwd))


def manage_accountants() -> None:
    """
    Opens accountant management screen
    """
    root = Tk()
    root.title("KinoRezIS")
    root.geometry("800x650+300+200")

    frame1 = LabelFrame(root, text="Seznam účetních")
    frame2 = LabelFrame(root, text="Vyhledávání")
    frame3 = LabelFrame(root, text="Informace a správa")
    for f in frame1, frame2, frame3:
        f.pack(fill="both", expand=1, padx=10, pady=10)

    table = __table(frame1)

    __namesearch(frame2, table)

    __management(frame3, table)

    root.mainloop()
