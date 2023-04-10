from gui_and_logic.login import login
from constants import ADMIN, ACCOUNTANT


def main() -> int:
    logged_user = login()
    if logged_user == ADMIN:
        print("admin logged")
        pass
    elif logged_user == ACCOUNTANT:
        print("accountant_logged")
        pass
    else:
        return -1
    return 0


if __name__ == "__main__":
    print(main())
