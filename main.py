from gui_and_logic import login, admin_options, accountant_options
from gui_and_logic import add_showtime
from constants import ADMIN, ACCOUNTANT
from constants import ADD_SHOWTIME, ADD_RESERVATION,\
                        MANAGE_ACCOUNTANTS, REMOVE_RESERVATION


def admin() -> None:
    while (True):
        chosen_option = admin_options()
        if chosen_option == ADD_SHOWTIME:
            add_showtime()
        elif chosen_option == MANAGE_ACCOUNTANTS:
            pass
        else:
            break


def accountant() -> None:
    while (True):
        chosen_option = accountant_options()
        if chosen_option == ADD_RESERVATION:
            pass
        elif chosen_option == REMOVE_RESERVATION:
            pass
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
    print(main())
