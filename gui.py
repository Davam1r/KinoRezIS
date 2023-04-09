from tkinter import Tk, Label, Entry, Button, Frame
from typing import Any, Callable


__BASEFONT = ("Arial", 14)


def login(login_cmd: Callable[..., Any]) -> None:
    root = Tk()
    root.title("KinoRezIS")
    root.geometry("400x300")

    frame = Frame()
    frame.pack(pady=30)

    login_label = Label(frame, text="login: ", font=__BASEFONT)
    login_label.grid(row=0, column=0)
    password_label = Label(frame, text="heslo: ", font=__BASEFONT)
    password_label.grid(row=1, column=0)

    login_entry = Entry(frame, font=__BASEFONT)
    login_entry.grid(row=0, column=1, pady=20)
    password_entry = Entry(frame, show="*", font=__BASEFONT)
    password_entry.grid(row=1, column=1)

    button = Button(frame, text="Přihlásit", font=("Arial", 15),
                    command=lambda: login_cmd(root))
    button.grid(row=2, pady=20, columnspan=2)

    root.mainloop()
