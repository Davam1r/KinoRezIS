from tkinter import Tk, Label, Entry, Button, Frame, messagebox
from constants import BASEFONT, ADMIN, ACCOUNTANT


__logged_user = 0


def __is_accountant() -> bool:
    # TODO
    return False


def __is_admin() -> bool:
    # TODO
    return False


def __user_verification(root: Tk) -> None:
    global __logged_user
    if __is_admin():
        __logged_user = ADMIN
        root.destroy()
        return
    if __is_accountant():
        __logged_user = ACCOUNTANT
        root.destroy()
        return
    messagebox.showinfo("error", "neexistující uživatel")
    return


def login() -> int:
    root = Tk()
    root.title("KinoRezIS")
    root.geometry("400x300")

    frame = Frame()
    frame.pack(pady=30)

    login_label = Label(frame, text="login: ", font=BASEFONT)
    login_label.grid(row=0, column=0)
    password_label = Label(frame, text="heslo: ", font=BASEFONT)
    password_label.grid(row=1, column=0)

    login_entry = Entry(frame, font=BASEFONT)
    login_entry.grid(row=0, column=1, pady=20)
    password_entry = Entry(frame, show="*", font=BASEFONT)
    password_entry.grid(row=1, column=1)

    button = Button(frame, text="Přihlásit", font=("Arial", 15),
                    command=lambda: __user_verification(root))
    button.grid(row=2, pady=20, columnspan=2)

    root.mainloop()

    return __logged_user
