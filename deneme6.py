import tkinter as tk


class IPEntry(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, borderwidth=1, relief="sunken",
                          background="white")
        self.entries = []
        for i in range(4):
            entry = tk.Entry(self, width=3, borderwidth=0,
                             justify="center",
                             highlightthickness=0, background="white")
            entry.pack(side="left")
            self.entries.append(entry)

            if i < 3:
                dot = tk.Label(self, text=".", background="white")
                dot.pack(side="left")

    def get(self):
        return ".".join([entry.get() for entry in self.entries])


root = tk.Tk()
field = IPEntry(root)
field.pack(side="top")
root.mainloop()
