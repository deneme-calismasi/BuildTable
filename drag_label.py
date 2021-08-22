from tkinter import *


def showPosEvent(event):
    print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))


def onLeftDrag(event):
    print('Got left mouse button drag:', showPosEvent(event))


root = Tk()
labelfont = ('courier', 20, 'bold')
widget = Label(root, text='Hello bind world')
widget.config(bg='red', font=labelfont)
widget.config(height=5, width=20)
widget.pack(expand=YES, fill=BOTH)

widget.bind('<B1-Motion>', onLeftDrag)

widget.focus()
root.title('Click Me')
root.mainloop()
