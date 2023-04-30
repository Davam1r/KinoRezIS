from constants import (ACCOUNTANT, ADD_RESERVATION, ADD_SHOWTIME, ADMIN,
                       MANAGE_ACCOUNTANTS, REMOVE_RESERVATION)
from gui_and_logic import (accept_reservations, accountant_options,
                           add_reservations, add_showtime, admin_options,
                           login, manage_accountants)


def admin() -> None:
    while (True):
        chosen_option = admin_options()
        if chosen_option == ADD_SHOWTIME:
            add_showtime()
        elif chosen_option == MANAGE_ACCOUNTANTS:
            manage_accountants()
        else:
            break


def accountant() -> None:
    while (True):
        chosen_option = accountant_options()
        if chosen_option == ADD_RESERVATION:
            add_reservations()
        elif chosen_option == REMOVE_RESERVATION:
            accept_reservations()
        else:
            break


def main() -> int:
    logged_user = login()
    if logged_user == ADMIN:
        admin()
    elif logged_user == ACCOUNTANT:
        accountant()
    else:
        return -1
    return 0


if __name__ == "__main__":
    main()
