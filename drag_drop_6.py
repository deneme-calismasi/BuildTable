import tkinter as tk
from tkinter import ttk


def swap(tv, col1, col2):
    dcols = list(tv["displaycolumns"])
    if dcols[0] == "#all":
        dcols = list(tv["columns"])
    id1 = tree.column(col1, 'id')
    id2 = tree.column(col2, 'id')
    i1 = dcols.index(id1)
    i2 = dcols.index(id2)
    dcols[i1] = id2
    dcols[i2] = id1
    tv["displaycolumns"] = dcols


def bDown(event):
    global dx, col_from_id
    tv = event.widget
    if tv.identify_region(event.x, event.y) != 'separator':
        col = tv.identify_column(event.x)
        col_from_id = tv.column(col, 'id')
        # get column x coordinate and width
        bbox = tv.bbox(tv.get_children("")[0], col_from_id)
        dx = bbox[0] - event.x  # distance between cursor and column left border
        #        tv.heading(col_from_id, text='')
        visual_drag.configure(displaycolumns=[col_from_id])
        visual_drag.place(in_=tv, x=bbox[0], y=0, anchor='nw', width=bbox[2], relheight=1)
    else:
        col_from_id = None


def bUp(event):
    visual_drag.place_forget()


def bMotion(event):
    tv = event.widget
    # drag around label if visible
    if visual_drag.winfo_ismapped():
        x = dx + event.x
        # middle of the dragged column
        xm = int(x + visual_drag.column('#1', 'width') / 2)
        visual_drag.place_configure(x=x)
        col = tv.identify_column(xm)
        # if the middle of the dragged column is in another column, swap them
        if tv.column(col, 'id') != col_from_id:
            swap(tv, col_from_id, col)


# Variable to hold initial choice of column to move
col_from = 0

root = tk.Tk()

# List of columns
columns = ["A", "B", "C", "D", "E", "F", "G"]

# Create treeview with columns. Display all columns
tree = ttk.Treeview(root, columns=columns, show='headings')  # , displaycolumns=columns)
# treeview to show column motion
visual_drag = ttk.Treeview(root, columns=columns, show='headings')
# Set headers
for col in columns:
    tree.heading(col, text=col)
    visual_drag.heading(col, text=col)

# insert some items into the tree
for i in range(10):
    tree.insert('', 'end', iid='line%i' % i,
                values=(i, i + 10, i + 20, i + 30, i + 40, i + 50, i + 60))
    visual_drag.insert('', 'end', iid='line%i' % i,
                       values=(i, i + 10, i + 20, i + 30, i + 40, i + 50, i + 60))

tree.grid()
tree.bind("<ButtonPress-1>", bDown)
tree.bind("<ButtonRelease-1>", bUp)
tree.bind("<Motion>", bMotion)

root.mainloop()
