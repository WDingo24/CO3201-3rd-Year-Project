from .. import root

import abc

import tkinter as tk

class State(abc.ABC):
    def __init__(self) -> None:
        self.frame = tk.Frame(root)
        self.frame.pack()

class CfgState(State):
    pass

from .complex import *
from .main import *
from .simple import *