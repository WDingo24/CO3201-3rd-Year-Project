from . import root
from . import states

from tkinter import Tk

if __name__ == "__main__":
    root.currentState.push(states.Menu())
    root.mainloop()