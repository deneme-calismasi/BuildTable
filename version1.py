from tkinter import ttk
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry('480x630')
root.title("Sensor Insert")
root.grid()

tree = ttk.Treeview(root, selectmode='browse')
tree.grid(row=1, column=1, columnspan=4, padx=20, pady=20)
tree["columns"] = ("1", "2", "3")

tree['show'] = 'headings'

verscrlbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(xscrollcommand=verscrlbar.set)

tree.column("1", width=125, minwidth=30, anchor='c')
tree.column("2", width=65, minwidth=30, anchor='c')
tree.column("3", width=115, minwidth=30, anchor='c')

tree.heading("1", text="ID")
tree.heading("2", text="Sensor No")
tree.heading("3", text="IP")

i = 1
tree.insert("", 'end', iid=1,
            values=(i, 'Sensor No', 'Sensor IP'))

add_label = tk.Label(root, text='Add Sensor',
                     font=('Helvetica', 16), width=30, anchor="c")
add_label.grid(row=2, column=1, columnspan=4)

name_label = tk.Label(root, text='Sensor Name: ', width=10, anchor="c")
name_label.grid(row=3, column=1)

# add one text box
t1 = tk.Text(root, height=1, width=10, bg='white')
t1.grid(row=3, column=2)

# add list box for selection of class
options = StringVar(root)
options.set("")  # default value

l3 = tk.Label(root, text='IP: ', width=10)
l3.grid(row=5, column=1)

# add one text box
t3 = tk.Text(root, height=1, width=4, bg='white')
t3.grid(row=5, column=2)

b1 = tk.Button(root, text='Save', width=10,
               command=lambda: add_data())
b1.grid(row=6, column=2)
my_str = tk.StringVar()
l5 = tk.Label(root, textvariable=my_str, width=10)
l5.grid(row=8, column=1)


def add_data():
    my_name = t1.get("1.0", END)  # read name
    my_mark = t3.get("1.0", END)  # read mark

    global i
    i = i + 1
    tree.insert("", 'end',
                values=(i, my_name, my_mark))
    t1.delete('1.0', END)  # reset the text entry box
    t3.delete('1.0', END)  # reset the text entry box
    my_str.set("Data added ")
    t1.focus()
    l5.after(3000, lambda: my_str.set(''))  # remove the message


root.mainloop()
