import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("TreeView Test")
root.resizable(False, False)
root.geometry("600x600")

selector = ttk.Treeview(root, selectmode="browse", show="tree")

def updateLabel(event) -> None:
    print(selector.bbox(selector.selection()[0]))
    print(selector.selection())

selector.insert("", "end", "one", text="One")
selector.insert("", "end", "two", text="Two")

selector.pack()

selector.bind("<<TreeviewSelect>>", updateLabel)

root.mainloop()