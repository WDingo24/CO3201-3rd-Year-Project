import tkinter as tk

class Window(tk.Tk):
    def __init__(self, cnf: dict={}, **kwargs):
        kwargs = cnf or kwargs
        super().__init__(**kwargs)