import tkinter as tk


class DragToplevel(tk.Toplevel):
    def __init__(self, master, image, x, y):
        tk.Toplevel.__init__(self, master)
        self.overrideredirect(True)
        self.geometry('+%i+%i' % (x, y))

        self.image = image

        self.label = tk.Label(self, image=image, bg='red')
        self.label.pack()

    def move(self, x, y):
        self.geometry('+%i+%i' % (x, y))


root = tk.Tk()

can1 = tk.Canvas(root, width=300, height=300, bg='white')
can2 = tk.Canvas(root, width=300, height=300, bg='white')

can1.pack(side='left')
can2.pack(side='right')
root.geometry('800x800')

# im = tk.PhotoImage('tux', master=root, file='/home/juliette/Images/tux_mini.png')
drag_id = ''
dragged = None
# can1.create_image(100, 200, image=im)


def click1(event):
    global drag_id, dragged
    items = can1.find_closest(event.x, event.y)
    if items:
        image = can1.itemcget(items[0], 'image')
        dragged = DragToplevel(root, image, event.x_root, event.y_root)
        drag_id = root.bind('<Motion>', lambda e: dragged.move(e.x_root, e.y_root))


def release(event):
    global drag_id, dragged
    root.unbind('<Motion>', drag_id)
    drag_id = ""
    xr, yr = event.x_root, event.y_root
    x2, y2 = can2.winfo_rootx(), can2.winfo_rooty()
    w2, h2 = can2.winfo_width(), can2.winfo_height()
    if dragged and xr >= x2 and xr < x2 + w2 and yr >= y2 and yr < y2 + h2:
        can2.create_image(xr - x2, yr - y2, image=dragged.image, anchor='nw')
    if dragged:
        dragged.destroy()
        dragged = None


can1.bind('<ButtonPress-1>', click1)
root.bind('<ButtonRelease-1>', release)

root.mainloop()
