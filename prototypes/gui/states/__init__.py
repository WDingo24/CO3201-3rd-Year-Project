from .. import root, defaultFont
from .. import widgets

import tkinter as tk
from tkinter import ttk

class State:
    def __init__(self) -> None:
        self.frame = ttk.Frame(root)
        self.frame.pack()

    def _switchBack(self) -> None:
        self.frame.destroy()
        root.currentState.pop()
        root.currentState.peek().frame.pack()

class Menu(State):
    def __init__(self) -> None:
        super().__init__()

        headingFont = defaultFont.copy()
        headingFont.config(size=30)
        ttk.Label(self.frame,
                 text="Digital Arithmetic\nAnimation Generator",
                 font=headingFont,
                 justify="center"
        ).grid(row=0, column=0, columnspan=2)

        ttk.Button(self.frame,
                   text="Simple",
                   command=self.__switchSimple
        ).grid(row=1, column=0)
        ttk.Button(self.frame,
                   text="Complex",
                   state="disabled"
        ).grid(row=1, column=1)

    def __switchSimple(self) -> None:
        self.frame.pack_forget()
        root.currentState.push(Simple())

class Simple(State):
    configFrames = {
        "Addition": widgets.AdditionCfgFrame,
        "Subtraction": ttk.Frame,
        "Multiplication": ttk.Frame,
        "Division": ttk.Frame
    }

    def __init__(self) -> None:
        super().__init__()

        ttk.Button(self.frame, text="Back", command=self._switchBack).pack()

        self.__currentCfg = ""
        self.__configFrame: ttk.Frame | None = None

        self.__selector = ttk.Combobox(self.frame,
                                       state="readonly",
                                       width=10,
                                       values=list(Simple.configFrames.keys()))
        self.__selector.bind("<<ComboboxSelected>>", self.__changeCfg)

        self.__container = ttk.LabelFrame(self.frame,
                                          labelwidget=self.__selector,
                                          width=350,
                                          height=350)

        self.__container.pack_propagate(False)
        self.__container.pack()

    def __changeCfg(self, event) -> None:
        val = self.__selector.get()

        if val == self.__currentCfg:
            return

        self.__currentCfg = val

        if self.__configFrame:
            self.__configFrame.pack_forget()

        self.__configFrame = Simple.configFrames[val](self.__container)

        self.__configFrame.pack()