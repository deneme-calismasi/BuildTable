import datetime as dt
import tkinter as tk
from tkinter import *
from tkinter import ttk

time_data = dt.datetime.now().strftime('%Y-%m-%d %X')

root = tk.Tk()
root.geometry('540x600')
root.title("Sensor Insert")
root.grid()

tree = ttk.Treeview(root, selectmode='browse')
tree.grid(row=1, column=1, columnspan=4, padx=20, pady=20)
tree["columns"] = ("1", "2", "3", "4")

tree['show'] = 'headings'

verscrlbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(xscrollcommand=verscrlbar.set)

tree.column("1", width=125, minwidth=30, anchor='c')
tree.column("2", width=125, minwidth=30, anchor='c')
tree.column("3", width=125, minwidth=30, anchor='c')
tree.column("4", width=125, minwidth=30, anchor='c')

tree.heading("1", text="ID")
tree.heading("2", text="Sensor No")
tree.heading("3", text="IP")
tree.heading("4", text="Time")

i = 1
tree.insert("", 'end', iid=1,
            values=(i, 'Sensor No', 'Sensor IP', str(time_data)))

add_label = tk.Label(root, text='Add Sensor',
                     font=('Helvetica', 16), width=30, anchor="c")
add_label.grid(row=2, column=1, columnspan=4)

name_label = tk.Label(root, text='Sensor Name: ', width=10, anchor="c")
name_label.grid(row=3, column=1)

# add one text box
t1 = tk.Text(root, height=1, width=10, bg='white')
t1.grid(row=3, column=2)

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
    sensor_name = t1.get("1.0", END)  # read name
    sensor_ip = t3.get("1.0", END)  # read mark

    global i
    i = i + 1
    tree.insert("", 'end',
                values=(i, sensor_name, sensor_ip, str(time_data)))
    t1.delete('1.0', END)  # reset the text entry box
    t3.delete('1.0', END)  # reset the text entry box
    my_str.set("Data added ")
    t1.focus()
    l5.after(3000, lambda: my_str.set(''))  # remove the message


root.mainloop()
