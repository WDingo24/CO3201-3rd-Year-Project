from . import root
from . import states

if __name__ == "__main__":
    root.currentState = states.Menu()
    root.mainloop()