import tkinter.ttk as ttk
from tkinter import *

root = Tk()


def OnDoubleClick(event):
    item = tree.identify("item", event.x, event.y)
    print("you clicked on", tree.item(item)["text"])


tree = ttk.Treeview(root)

tree["columns"] = ("one", "two")
tree.heading("one", text="coulmn A")
tree.heading("two", text="column B")

tree.insert("", 3, "dir3", text="Dir 3", values=("3A", " 3B"))
tree.insert("dir3", 3, 'subdir3', text="sub dir 3", values=("3A", " 3B"))

tree.bind("<Double-1>", OnDoubleClick)

tree.pack()
root.mainloop()
