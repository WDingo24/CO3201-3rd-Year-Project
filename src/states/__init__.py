from .. import root

import tkinter as tk

class State:
    def __init__(self) -> None:
        self.frame = tk.Frame(root)
        self.frame.pack()

    def _switchBack(self) -> None:
        self.frame.destroy()
        root.currentState.pop()
        root.currentState.peek().frame.pack()

class Menu(State):
    def __init__(self) -> None:
        super().__init__()

        tk.Label(self.frame, text="Test").pack()