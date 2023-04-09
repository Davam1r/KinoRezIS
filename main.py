from tkinter import Tk
import gui


def foo(root: Tk) -> None:
    print("finished")
    root.destroy()


def main() -> None:
    gui.login(foo)
