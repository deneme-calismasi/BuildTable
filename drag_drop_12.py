from tkinter import *


class ToggleButton(Canvas):
    def __init__(self, root, command=None, fg='white', bg_off='#d9dadc', bg_on='#4ED164', state='on'):
        super().__init__()
        self.height = 50
        self.width = 100
        self.bg_on = bg_on
        self.bg_off = bg_off
        self.configure(width=self.width, height=self.height, borderwidth=0, highlightthickness=0)
        self.root = root
        self.state = state
        bg = self.bg_on if self.state == 'on' else self.bg_off

        self.left_side = self.create_arc(
            (0, 0, 0, 0), start=90, extent=180, fill=bg, outline=bg)
        self.right_side = self.create_arc(
            (0, 0, 0, 0), start=-90, extent=180, fill=bg, outline=bg)
        self.rect = self.create_rectangle(0, 0, 0, 0, fill=bg, outline=bg)
        self.btn = self.create_oval(0, 0, 0, 0, fill=fg, outline=bg)

        self.bind('<Configure>', self._resize)
        self.bind('<Button>', self._animate, add='+')
        self.bind('<Button>', command, add='+')

    def _animate(self, event):
        x, y, w, h = self.coords(self.btn)
        x = int(x - 1)
        y = int(y - 1)
        offset = 4
        if x == self.coords(self.right_side)[0] + offset:
            self.moveto(self.btn, offset, offset)
            self.state = 'off'
            self._update_bg(self.bg_off)
        else:
            self.moveto(self.btn, self.coords(self.right_side)[0] + offset, offset)
            self.state = 'on'
            self._update_bg(self.bg_on)

    def _update_bg(self, color):
        for bg_item in [self.left_side, self.right_side, self.rect]:
            self.itemconfig(bg_item, fill=color, outline=color)
        self.itemconfig(self.btn, outline=color)

    def _resize(self, event):
        # scale controls, in part, the y-axis placement of the button on the toggle
        scale = 5
        self.coords(self.left_side, scale, scale, event.height - scale, event.height - scale)
        self.coords(self.right_side, scale, scale, event.height, event.height - scale)
        self.coords(self.btn, scale, scale, event.height - scale, event.height - scale)
        factor = event.width - (2 * scale) - \
                 (self.coords(self.right_side)[2] - self.coords(self.right_side)[0])
        self.move(self.right_side, factor, 0)
        self.coords(self.rect,
                    self.bbox(self.left_side)[2] - 2,
                    scale,
                    self.bbox(self.right_side)[0] + 2,
                    event.height - scale)

        self.moveto(self.btn, self.coords(self.right_side)[0] + 4, 4)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value


def hello(event='') -> None:
    if btn.state == 'on':
        btn.state = 'off'
    else:
        btn.state = 'on'
    print(f'State is {btn.state}')


root = Tk()
btn = ToggleButton(root, lambda _: hello('Hello'), 'red', 'green')
btn.pack()

btn2 = ToggleButton(root, command=hello)
btn2.pack(expand=True, fill='both')

Button(root, text='Text').pack(expand=True, fill='both')

root.mainloop()
