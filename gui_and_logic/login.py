from tkinter import Button, Entry, Frame, Label, Tk, messagebox

from constants import (ACCOUNTANT, ADMIN, ADMIN_LOGIN, ADMIN_PASSWORD,
                       BASEFONT, BUTTONFONT)
from databaseSDK.accountants import accountant_login_exists as __is_accountant

__logged_user = 0


def __is_admin(login: str, password: str) -> bool:
    return login == ADMIN_LOGIN and password == ADMIN_PASSWORD


def __user_verification(root: Tk, login: str, password: str) -> None:
    global __logged_user
    if __is_admin(login, password):
        __logged_user = ADMIN
        root.destroy()
        return
    if __is_accountant(login, password):
        __logged_user = ACCOUNTANT
        root.destroy()
        return
    messagebox.showerror("error", "neexistující uživatel")
    return


def login() -> int:
    """
    Initiates login screen and handles user verification

    @return int value representing the user
    """
    root = Tk()
    root.title("KinoRezIS")
    root.geometry("400x300+400+300")

    frame = Frame()
    frame.pack(pady=30)

    log_label = Label(frame, text="login: ", font=BASEFONT)
    log_label.grid(row=0, column=0)
    pass_label = Label(frame, text="heslo: ", font=BASEFONT)
    pass_label.grid(row=1, column=0)

    log_entry = Entry(frame, font=BASEFONT)
    log_entry.grid(row=0, column=1, pady=20)
    pass_entry = Entry(frame, show="*", font=BASEFONT)
    pass_entry.grid(row=1, column=1)

    button = Button(frame, text="Přihlásit", font=BUTTONFONT,
                    command=lambda: __user_verification(root,
                                                        log_entry.get(),
                                                        pass_entry.get()))
    button.grid(row=2, pady=20, columnspan=2)
    root.bind("<Return>",  # enter key can act as button press too
              lambda _: __user_verification(root,
                                            log_entry.get(),
                                            pass_entry.get()))

    root.mainloop()

    return __logged_user
