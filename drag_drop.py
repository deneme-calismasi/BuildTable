from tkinter import *
from tkinter.dnd import Tester as DragWindow, Icon as Dragable

# Make a root window and hide it, since we don't need it.
root = Tk()
root.withdraw()
# Make the actual main window, which can have dragable objects on.
main = DragWindow(root)


def make_btn():
    """Make a new test button."""
    # The functional part of the main window is the canvas.
    Dragable('B').attach(main.canvas)


# Make a button and bind it to our button creating function.
Button(main.top, text='A', command=make_btn).pack()
# Start the mainloop.
mainloop()
