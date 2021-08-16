from tkinter import *
import sqlite3

root = Tk()
conn = sqlite3.connect('my_database.db')
# create a table for testing
sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS my_table (
                                        name text
                                    ); """
conn.execute(sql_create_projects_table)


# function to be called when button is clicked
def savetodb():
    # txtName.get() will get the value in the entry box
    entry_name = txtName.get()
    conn.execute('insert into my_table(name) values (?)', (str(entry_name),))
    curr = conn.execute("SELECT name from my_table")
    print(curr.fetchone())


txtName = Entry(root)
txtName.pack()

# function savetodb will be called when button is clicked
btnSave = Button(root, text="Save", command=savetodb)
btnSave.pack()

root.mainloop()
