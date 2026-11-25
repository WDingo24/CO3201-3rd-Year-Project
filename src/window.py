import tkinter as tk

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import states

class Window(tk.Tk):
    def __init__(self, cnf: dict={}, **kwargs):
        kwargs = cnf or kwargs
        super().__init__(**kwargs)

        self.geometry("600x600")

        self.__currentState = None

    @property
    def currentState(self) -> "states.State":
        if self.__currentState is None:
            raise AttributeError

        return self.__currentState

    @currentState.setter
    def currentState(self, newState: "states.State"):
        if self.__currentState is not None:
            self.__currentState.frame.destroy()

        self.__currentState = newState
        self.__currentState.frame.pack()

    @currentState.deleter
    def currentState(self):
        if self.__currentState is not None:
            self.__currentState.frame.destroy()