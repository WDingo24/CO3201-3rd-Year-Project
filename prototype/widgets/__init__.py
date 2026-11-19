import tkinter as tk
from tkinter import ttk

class AdditionCfgFrame(ttk.Frame):
    def __init__(self,
                 master,
                 cnf: dict={},
                 **kwargs) -> None:
        kwargs = cnf or kwargs
        super().__init__(master, **kwargs)
        
        ttk.Label(self, text="Addition").grid(row=0, column=0, columnspan=2)

        ttk.Label(self, text="Operand 1").grid(row=1, column=0)
        ttk.Label(self, text="Operand 2").grid(row=1, column=1)

        self.__opEntry1 = ttk.Spinbox(self, from_=0, to=255, width=3)
        self.__opEntry2 = ttk.Spinbox(self, from_=0, to=255, width=3)

        self.__opEntry1.set(0)
        self.__opEntry2.set(0)

        self.__opEntry1.grid(row=2, column=0)
        self.__opEntry2.grid(row=2, column=1)

        ttk.Label(self, text="Animation Type").grid(row=3, column=0, columnspan=2)

        self.__animTypes = ["Written", "Hardware", "Both"]
        self.__animTypeEntry = ttk.Combobox(self,
                                     state="readonly",
                                     width=10,
                                     values=self.__animTypes)

        self.__animTypeEntry.current(0)

        self.__animTypeEntry.grid(row=4, column=0, columnspan=2)

        ttk.Button(self,
                   text="Generate",
                   command=self.__generate
        ).grid(row=5, column=0, columnspan=2)

    def __generate(self) -> None:
        with open("output.txt", "w") as file:
            file.write(f"op1={int(self.__opEntry1.get()):08b}\n")
            file.write(f"op2={int(self.__opEntry2.get()):08b}\n")
            file.write(f"animType={self.__animTypes.index(
                self.__animTypeEntry.get())}")