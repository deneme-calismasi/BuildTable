import datetime as dt
import tkinter as tk
from tkinter import *
from tkinter import ttk


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.root = tk.Tk()
        self.tree = ttk.Treeview(self.root, selectmode='extended')

        self.tree["columns"] = ("1", "2", "3", "4")
        self.tree.column("1", width=125, minwidth=30, anchor='c')
        self.tree.column("2", width=125, minwidth=30, anchor='c')
        self.tree.column("3", width=125, minwidth=30, anchor='c')
        self.tree.column("4", width=125, minwidth=30, anchor='c')

        self.tree.bind('<ButtonRelease-1>', self.selectItem)

        self.tree.heading("1", text="ID")
        self.tree.heading("2", text="Sensor No")
        self.tree.heading("3", text="IP")
        self.tree.heading("4", text="Time")

        self.tree['show'] = 'headings'

        self.root.geometry('540x400')
        self.root.title("Sensor Insert")
        self.root.grid()

        self.tree.grid(row=1, column=1, columnspan=4, padx=20, pady=20)

        verscrlbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(xscrollcommand=verscrlbar.set)

        self.time_data = dt.datetime.now().strftime('%Y-%m-%d %X')

        self.add_label = tk.Label(self.root, text='Add Sensor',
                                  font=('Helvetica', 16), width=30, anchor="c")
        self.add_label.grid(row=2, column=1, columnspan=4)

        self.name_label = tk.Label(self.root, text='Sensor No: ', width=10, anchor="c")
        self.name_label.grid(row=3, column=1)

        self.t1 = tk.Text(self.root, height=1, width=16, bg='white')
        self.t1.grid(row=3, column=2)

        self.l3 = tk.Label(self.root, text='Sensor IP: ', width=10)
        self.l3.grid(row=5, column=1)

        self.t3 = tk.Text(self.root, height=1, width=16, bg='white')
        self.t3.grid(row=5, column=2)

        self.b1 = tk.Button(self.root, text='Save', width=10,
                            command=lambda: self.add_data())
        self.b1.grid(row=6, column=2)
        self.my_str = tk.StringVar()

        self.l5 = tk.Label(self.root, textvariable=self.my_str, width=10)
        self.l5.grid(row=8, column=1)
        self.i = 0

        # self.root.mainloop()

    def selectItem(self, event):
        global cell_value
        curItem = self.tree.item(self.tree.focus())
        col = self.tree.identify_column(event.x)
        print('curItem = ', curItem)
        print('col = ', col)

        if col == '#0':
            cell_value = curItem['text']
        elif col == '#1':
            cell_value = curItem['values'][0]
        elif col == '#2':
            cell_value = curItem['values'][1]
        elif col == '#3':
            cell_value = curItem['values'][2]
        elif col == '#4':
            cell_value = curItem['values'][3]
        print('cell_value = ', cell_value)

    def add_data(self):
        sensor_name = self.t1.get("1.0", END)
        sensor_ip = self.t3.get("1.0", END)

        global i
        self.i = self.i + 1
        self.tree.insert("", 'end',
                         values=(int(self.i), sensor_name, sensor_ip, str(self.time_data)))

        self.t1.delete('1.0', END)  # reset the text entry box
        self.t3.delete('1.0', END)  # reset the text entry box
        self.my_str.set("Sensor Added !")
        self.t1.focus()

        self.l5.after(3000, lambda: self.my_str.set(''))  # remove the message


'''def record_data():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Sensor_Record"]

    mycol = mydb["data1"]

    mycol.insert_one()
'''
'''if __name__ == "__main__":
    app = App()
    app.mainloop()'''

'''def main(): #run mianloop 
    root = tk.Tk()
    app = Window1(root)
    root.mainloop()

if __name__ == '__main__':
    main()'''

app = App()
app.mainloop()
