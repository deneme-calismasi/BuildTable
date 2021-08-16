from tkinter import *
from tkinter import ttk


class Task:

    def __init__(self, subject=None, priority=None):
        self.subject = subject
        self.priority = priority


class Todo(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.title('Todo')
        self.master.geometry('237x306')
        self.create_widgets()
        self.tasks = []

    def create_widgets(self):
        self.search_frame = Frame(self.master)
        self.search_frame.grid(row=0)

        self.treeview_frame = Frame(self.master)
        self.treeview_frame.grid(row=1)

        self.buttons_frame = Frame(self.master)
        self.buttons_frame.grid(row=2)

        self.search_text = Entry(self.search_frame,
                                 width=29)
        self.search_text.grid(row=0)

        self.treeview = ttk.Treeview(self.treeview_frame,
                                     height=12,
                                     columns=('Subject', 'Priority'))
        self.treeview.grid(row=0)
        self.treeview.column('#0', minwidth=0, width=30, stretch=NO)
        self.treeview.heading('#0', text="#")
        self.treeview.column('Subject', minwidth=0, width=147, stretch=NO)
        self.treeview.heading('Subject', text='Subject')
        self.treeview.column('Priority', minwidth=0, width=57, stretch=NO)
        self.treeview.heading('Priority', text='Priority')
        self.i = 0

        self.add_button = Button(self.buttons_frame,
                                 text='Add',
                                 command=self.add_item)
        self.add_button.grid(row=0, column=0)

        self.remove_button = Button(self.buttons_frame,
                                    text='Remove',
                                    command=self.remove_item)

        self.remove_button.grid(row=0, column=1)

        self.edit_button = Button(self.buttons_frame,
                                  text='Edit',
                                  command=self.edit_item)
        self.edit_button.grid(row=0, column=2)

        self.save_button = Button(self.buttons_frame,
                                  text='Save',
                                  command=self.save_item)
        self.save_button.grid(row=0, column=3)

    def create_item_dialog(self):
        self.item_dialog = Toplevel(self.master)
        self.item_dialog.geometry('202x197')

        self.item_dialog_text_frame = Frame(self.item_dialog)
        self.item_dialog_text_frame.grid(row=0, sticky=W)

        self.item_dialog_combobox_frame = Frame(self.item_dialog)
        self.item_dialog_combobox_frame.grid(row=1, sticky=W)

        self.item_dialog_another_frame = Frame(self.item_dialog)
        self.item_dialog_another_frame.grid(row=2)

        self.item_dialog_buttons_frame = Frame(self.item_dialog)
        self.item_dialog_buttons_frame.grid(row=3)

        self.subject_label = Label(self.item_dialog_text_frame,
                                   text='Subject:')
        self.subject_label.grid(row=0, sticky=W)

        self.subject_text = Text(self.item_dialog_text_frame,
                                 width=28,
                                 height=9)
        self.subject_text.grid(row=1)

        self.priority_label = Label(self.item_dialog_combobox_frame,
                                    text='Priority:')

        self.priority_label.grid(row=0, column=0, sticky=W)

        self.priority_combobox = ttk.Combobox(self.item_dialog_combobox_frame,
                                              width=17)
        self.priority_combobox.grid(row=0, column=1)
        self.priority_combobox['values'] = ('High', 'Medium', 'Low')

        self.item_dialog_ok_button = Button(self.item_dialog_buttons_frame,
                                            width=9,
                                            text='OK',
                                            command=self.add)
        self.item_dialog_ok_button.grid(row=0, column=0)

        self.item_dialog_cancel_button = Button(self.item_dialog_buttons_frame,
                                                width=9,
                                                text='Cancel',
                                                command=self.close_item_dialog)
        self.item_dialog_cancel_button.grid(row=0, column=1)

        self.item_dialog.wait_window()

    def close_item_dialog(self):
        self.item_dialog.destroy()

    def add_item(self):
        self.create_item_dialog()

    def add(self):
        t = Task(self.subject_text.get('1.0', '1.0 lineend'), self.priority_combobox.get())

        self.treeview.insert('', END, text=str(self.i), values=(t.subject, t.priority))
        self.i = self.i + 1
        self.tasks.append(t)

        self.close_item_dialog()

    def remove_item(self):
        selected_items = self.treeview.selection()
        for selected_item in selected_items:
            self.treeview.delete(selected_item)

    def edit_item(self):
        pass

    def save_item(self):
        pass


def main():
    root = Tk()
    Todo(root)
    root.mainloop()


if __name__ == '__main__':
    main()
