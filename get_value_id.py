import tkinter.ttk as ttk
from tkinter import *

root = Tk()


def OnDoubleClick(event):
    print(tree.identify_row(event.y))


tree = ttk.Treeview(root)

tree["columns"] = ("one", "two")
tree.heading("one", text="coulmn A")
tree.heading("two", text="column B")

tree.insert("", 3, "dir3", text="Dir 3", values=("3A", " 3B"))
# tree.insert("dir3", 3, 'subdir3', text="sub dir 3", values=("3A", " 3B"))

for item in tree.selection():
    item_child = tree.get_children(item)
    item = tree.item(item)
    iid = tree.focus()
    print("iid = ", iid, "Item = ", item, "Child iid's =", item_child)

tree.bind("<Double-1>", OnDoubleClick)

tree.pack()
root.mainloop()
