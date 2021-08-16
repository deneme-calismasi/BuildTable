from tkinter import ttk
import tkinter as tk
from tkinter import *
import datetime as dt
import pymongo

time_data = dt.datetime.now().strftime('%Y-%m-%d %X')

root = tk.Tk()
root.geometry('540x400')
root.title("Sensor Insert")
root.grid()

tree = ttk.Treeview(root, selectmode='extended')
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

add_label = tk.Label(root, text='Add Sensor',
                     font=('Helvetica', 16), width=30, anchor="c")
add_label.grid(row=2, column=1, columnspan=4)

name_label = tk.Label(root, text='Sensor No: ', width=10, anchor="c")
name_label.grid(row=3, column=1)

t1 = tk.Text(root, height=1, width=16, bg='white')
t1.grid(row=3, column=2)

l3 = tk.Label(root, text='Sensor IP: ', width=10)
l3.grid(row=5, column=1)

t3 = tk.Text(root, height=1, width=16, bg='white')
t3.grid(row=5, column=2)

b1 = tk.Button(root, text='Save', width=10,
               command=lambda: add_data())
b1.grid(row=6, column=2)
my_str = tk.StringVar()

l5 = tk.Label(root, textvariable=my_str, width=10)
l5.grid(row=8, column=1)
i = 0

'''def record_data():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Sensor_Record"]

    mycol = mydb["data1"]

    mycol.insert_one()
'''


def add_data():
    sensor_name = t1.get("1.0", END)
    sensor_ip = t3.get("1.0", END)

    global i
    i = i + 1
    tree.insert("", 'end',
                values=(int(i), sensor_name, sensor_ip, str(time_data)))

    t1.delete('1.0', END)  # reset the text entry box
    t3.delete('1.0', END)  # reset the text entry box
    my_str.set("Sensor Added !")
    t1.focus()

    l5.after(3000, lambda: my_str.set(''))  # remove the message


root.mainloop()
