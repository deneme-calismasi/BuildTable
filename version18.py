import tkinter as tk
from tkinter import ttk
from tkinter import *
import datetime as dt
import pymongo


class Table(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('540x480')
        self.root.title("Sensor Insert")
        self.root.grid()
        self.style = ttk.Style()
        self.tree = ttk.Treeview(self.root, selectmode='extended')
        self.time_data = dt.datetime.now().strftime('%Y-%m-%d %X')
        self.primary_key = 0
        self.add_label = tk.Label(self.root, text='Add Sensor',
                                  font=('Helvetica', 16), width=30, anchor="c")
        self.name_label = tk.Label(self.root, text='Sensor No: ', width=10, anchor="c")
        self.t1 = tk.Text(self.root, height=1, width=16, bg='white')
        self.l3 = tk.Label(self.root, text='Sensor IP: ', width=10)
        self.t3 = tk.Text(self.root, height=1, width=16, bg='white')
        self.b1 = tk.Button(self.root, text='Save', width=10,
                            command=lambda: self.add_data())
        self.my_str = tk.StringVar()
        self.l5 = tk.Label(self.root, textvariable=self.my_str, width=10)
        self.d5 = tk.Button(self.root, text='Delete', width=10,
                            command=lambda: self.delete_data())
        self.k5 = tk.Button(self.root, text='Delete All', width=10,
                            command=lambda: self.delete_all())
        self.d6 = tk.Button(self.root, text='Add', width=10,
                            command=lambda: self.record_data())
        self.d7 = tk.Button(self.root, text='Fetch', width=10,
                            command=lambda: self.get_value_mongo())

    def window_table(self):
        self.tree["columns"] = ("1", "2", "3", "4")

        self.tree.column("1", width=125, minwidth=30, anchor='c')
        self.tree.column("2", width=125, minwidth=30, anchor='c')
        self.tree.column("3", width=125, minwidth=30, anchor='c')
        self.tree.column("4", width=125, minwidth=30, anchor='c')

        self.tree.heading("1", text="ID")
        self.tree.heading("2", text="Sensor No")
        self.tree.heading("3", text="IP")
        self.tree.heading("4", text="Time")

        self.tree['show'] = 'headings'

        self.tree.bind('<ButtonRelease-1>', self.select_item, self.record_data)

        self.tree.grid(row=1, column=1, columnspan=4, padx=20, pady=20)

        verscrlbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(xscrollcommand=verscrlbar.set)

        self.add_label.grid(row=2, column=1, columnspan=4)

        self.name_label.grid(row=3, column=1)

        self.t1.grid(row=3, column=2)
        self.l3.grid(row=5, column=1)
        self.t3.grid(row=5, column=2)
        self.b1.grid(row=6, column=2)
        self.l5.grid(row=8, column=1)
        self.d5.grid(row=8, column=2)
        self.k5.grid(row=10, column=2)
        self.d6.grid(row=8, column=3)
        self.d7.grid(row=8, column=4)

        return self.root.mainloop()

    def add_data(self):
        sensor_name = self.t1.get("1.0", END)
        sensor_ip = self.t3.get("1.0", END)

        global primary_key
        self.primary_key = self.primary_key + 1
        self.tree.insert("", 'end',
                         values=(int(self.primary_key), sensor_name, sensor_ip, str(self.time_data)))

        self.t1.delete('1.0', END)
        self.t3.delete('1.0', END)
        self.my_str.set("Sensor Added !")
        self.t1.focus()

        self.l5.after(3000, lambda: self.my_str.set(''))

    def delete_data(self):
        selected_item = self.tree.selection()[0]
        self.tree.delete(selected_item)
        print("Data deleted !")

    def delete_all(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["Sensor_Record"]
        mycol = mydb["data1"]

        mycol.delete_many({})

        for selected_item in self.tree.get_children():
            self.tree.delete(selected_item)

    def select_item(self, *args):
        global row_value
        curItem = self.tree.item(self.tree.focus())
        row_value = curItem['values']
        print('cell_value = ', row_value)
        return row_value

    def convert_data(self):
        products = [self.select_item()]
        arr = []
        for product in products:
            vals = {}
            vals["ID"] = int(product[0])
            vals["Sensor No"] = str(product[1])
            vals["IP"] = str(product[2])
            vals["Time"] = str(product[3])
            arr.append(vals)
        print("arr", arr)
        return arr

    def record_data(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["Sensor_Record"]

        mycol = mydb["data1"]

        print("reg", self.convert_data())
        a = self.convert_data()
        mycol.insert_many(a)

    def get_value_mongo(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["Sensor_Record"]
        mycol = mydb["data1"]
        mydoc_all = mycol.find()
        for mydoc_all in mycol.find():
            print(mydoc_all)
        print("get_value_mongo", mydoc_all)

    def show_data(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["Sensor_Record"]
        mycol = mydb["data1"]
        documents = list(mycol.find({}, {'_id': 0}))
        res = [list(idx.values()) for idx in documents]

        for index1, row in enumerate(res):
            for index2, item in enumerate(row):
                try:
                    res[index1][index2] = (int(item))
                except ValueError:
                    pass
        start_range = 1
        for rec in res:
            self.tree.insert("", index='end', iid=start_range, values=(int(rec[0]), rec[1], rec[2], str(rec[3])))
            start_range += 1


def main():
    app = Table()
    app.window_table()


if __name__ == '__main__':
    main()
