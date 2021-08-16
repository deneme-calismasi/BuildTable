from tkinter import *


class DragManager():
    listeDrop = []

    def __init__(self, widget, drag=True, drop=True):

        self.widget = widget

        self.drag = drag

        self.drop = drop

        if drag:
            self.add_dragable(self.widget)

        if drop:
            DragManager.listeDrop.append(self.widget)

    def add_dragable(self, widget):

        self.widget = widget

        self.widget.bind("<ButtonPress-1>", self.on_start)

        self.widget.bind("<B1-Motion>", self.on_drag)

        self.widget.bind("<ButtonRelease-1>", self.on_drop)

        self.widget["cursor"] = "hand1"

    def on_start(self, event):

        self.memoire = self.widget.cget("text")

        widgetDeplace = Label(fen_princ, text=self.memoire, fg="yellow", bg="grey", font=("Helvetica", 20), height=3,
                              width=5)

        self.icone = widgetDeplace

    def on_drag(self, event):

        xd = event.x_root

        yd = event.y_root

        self.icone.place(x=xd, y=yd)

    def on_drop(self, event):

        # commencons par trouver le widget sous le curseur de la souris

        x, y = event.widget.winfo_pointerxy()

        self.icone.destroy()

        target = event.widget.winfo_containing(x, y)

        if target in DragManager.listeDrop:

            try:

                target.configure(text=self.memoire)

            except:

                pass


# Création de la fenetre principale

fen_princ = Tk()

fen_princ.title("Ca drag et ça drop")

fen_princ.geometry("900x600")

# Création des 3 Labels sélectionnables

choix1 = Label(fen_princ, text="10", fg="yellow", bg="black", font=("Helvetica", 20), height=3, width=5)

choix2 = Label(fen_princ, text="20", fg="yellow", bg="black", font=("Helvetica", 20), height=3, width=5)

choix3 = Label(fen_princ, text="15", fg="yellow", bg="black", font=("Helvetica", 20), height=3, width=5)

choix1.place(x=50, y=50)

choix2.place(x=200, y=50)

choix3.place(x=350, y=50)

# Création des 3 Labels dropables

zoneDrop1 = Label(fen_princ, text="", fg="yellow", bg="black", font=("Helvetica", 20), height=3, width=5)

zoneDrop2 = Label(fen_princ, text="", fg="yellow", bg="black", font=("Helvetica", 20), height=3, width=5)

zoneDrop3 = Label(fen_princ, text="", fg="yellow", bg="black", font=("Helvetica", 20), height=3, width=5)

zoneDrop1.place(x=50, y=250)

zoneDrop2.place(x=200, y=250)

zoneDrop3.place(x=350, y=250)

drag1 = DragManager(choix1, drag=True, drop=False)

drag2 = DragManager(choix2, drag=True, drop=False)

drag3 = DragManager(choix3, drag=True, drop=False)

drop1 = DragManager(zoneDrop1, drag=False, drop=True)

drop2 = DragManager(zoneDrop2, drag=False, drop=True)

drop3 = DragManager(zoneDrop3, drag=False, drop=True)

# Lancement de la surveillance sur la fenêtre

fen_princ.mainloop()
