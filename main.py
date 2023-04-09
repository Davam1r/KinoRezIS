from gui_and_logic.login import login
from constants import ADMIN, ACCOUNTANT


def main() -> int:
    logged_user = login()
    if logged_user == ADMIN:
        pass
    elif logged_user == ACCOUNTANT:
        pass
    else:
        return -1
    return 0


if __name__ == "__main__":
    print(main())
