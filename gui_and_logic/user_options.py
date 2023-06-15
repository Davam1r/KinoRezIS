from tkinter import Button, Frame, Tk
from typing import Callable

from constants import (ADD_RESERVATION, ADD_SHOWTIME, BUTTONFONT,
                       MANAGE_ACCOUNTANTS, REMOVE_RESERVATION)

__selected_option = 0


def __add_showtime(root: Tk) -> None:
    """
    Sets module-private global variable to a value which represents
    that functionality to add a Showtime was chosen

    Destroys option selection GUI window on success

    @param root GUI window
    """
    global __selected_option
    __selected_option = ADD_SHOWTIME
    root.destroy()


def __manage_accountants(root: Tk) -> None:
    """
    Sets module-private global variable to a value which represents
    that functionality to manage accountants was chosen

    Destroys option selection GUI window on success

    @param root GUI window
    """
    global __selected_option
    __selected_option = MANAGE_ACCOUNTANTS
    root.destroy()


def __add_reservation(root: Tk) -> None:
    """
    Sets module-private global variable to a value which represents
    that functionality to add a Reservation was chosen

    Destroys option selection GUI window on success

    @param root GUI window
    """
    global __selected_option
    __selected_option = ADD_RESERVATION
    root.destroy()


def __remove_reservation(root: Tk) -> None:
    """
    Sets module-private global variable to a value which represents
    that functionality to remove a Reservation was chosen

    Destroys option selection GUI window on success

    @param root GUI window
    """
    global __selected_option
    __selected_option = REMOVE_RESERVATION
    root.destroy()


def __two_buttons(root: Tk,
                  txt1: str, cmd1: Callable[[], None],
                  txt2: str, cmd2: Callable[[], None]) -> None:
    """
    Draws two buttons with specified text and function
    on a specified GUI window

    @param root GUI window
    @param text for button1
    @param function for button 1
    @param text for button 2
    @param function for button 2
    """
    root.geometry("400x300+400+300")

    frame = Frame()
    frame.pack(pady=50)

    b1 = Button(frame, text=txt1, font=BUTTONFONT,
                command=cmd1)
    b1.pack(pady=20)

    b2 = Button(frame, text=txt2, font=BUTTONFONT,
                command=cmd2)
    b2.pack(pady=20)

    root.mainloop()


def admin_options() -> int:
    """
    Draws admin options screen

    @return int value representing chosen option
    """
    global __selected_option
    __selected_option = 0

    root = Tk()
    root.title("KinoRezIS - ADMIN")

    __two_buttons(root,
                  "Přidat promítací termín", lambda: __add_showtime(root),
                  "Spravovat účetní", lambda: __manage_accountants(root))

    return __selected_option


def accountant_options() -> int:
    """
    Draws accountant options screen

    @return int value representing chosen option
    """
    global __selected_option
    __selected_option = 0

    root = Tk()
    root.title("KinoRezIS - ÚČETNÍ")

    __two_buttons(root,
                  "Zapsat rezervaci", lambda: __add_reservation(root),
                  "Kontrola rezervací", lambda: __remove_reservation(root))

    return __selected_option
