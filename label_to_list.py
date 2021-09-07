import tkinter as tk
from tkinter import ttk
from tkinter import *

root = tk.Tk()
labels = []
name_label = tk.Label(root, text='Sensor No: ', width=10, anchor="c")
t1 = tk.Text(root, height=1, width=16, bg='white')
name_label.place(x=250, y=250)
t1.grid(row=3, column=2)


def button_click():
    labels.append(t1.get("1.0", 'end-1c'))
    t1.delete("1.0", 'end-1c')
    print(labels)


b1 = tk.Button(root, text='Add', width=10,
               command=lambda: button_click())

b1.grid(row=6, column=2)
root.mainloop()
