from tkinter import *

root = Tk()

grid = Frame(root)
grid.pack()

img0 = PhotoImage(file="0.png")
img1 = PhotoImage(file="1.png")
img2 = PhotoImage(file="2.png")

fill = 1


class button:

    def __init__(self, x, y):

        self.type = 0

        self.but = Button(grid, command=self.change, image=img0, borderwidth=0)
        self.but.grid(row=y, column=x)

        # Changed
        self.already_changed = False

    def change(self):
        if self.type == fill:
            self.but.config(image=img0)
            self.type = 0
        else:
            self.but.config(
                image=eval("img" + str(fill)))  # I left this in here, but you should NEVER use eval(). It's unsafe.
            self.type = fill

    # Changed
    def mouse_entered(self):
        if not self.already_changed:
            self.change()
            self.already_changed = True

    def mouse_up(self):
        self.already_changed = False


# Changed
class Container:
    def __init__(self, x, y):
        grid_buttons = []

        for Y in range(y):
            grid_buttons.append([])
            for X in range(x):
                grid_buttons[Y].append(button(X, Y))

        self.buttons = grid_buttons
        grid.bind_all("<Button-1>", self.mouse_down)
        grid.bind_all("<ButtonRelease-1>", self.mouse_up)
        grid.bind_all("<B1-Motion>", self.mouse_motion)
        self.mouse_pressed = False

    def mouse_down(self, e):
        self.mouse_pressed = True

    def mouse_up(self, e):
        self.mouse_pressed = False
        for row in self.buttons:
            for but in row:
                but.mouse_up()

    def mouse_motion(self, e):
        for row in self.buttons:
            for but in row:
                if grid.winfo_containing(e.x_root, e.y_root) is but.but:
                    but.mouse_entered()


container = Container(15, 15)

root.mainloop()
