import tkinter as tk

root = tk.Tk()

margin = 0.23

entry = tk.Entry(root)

entry.pack()


def profit_calculator():
    profit = margin * int(entry.get())
    print(profit)


button_calc = tk.Button(root, text="Calculate", command=profit_calculator)
button_calc.pack()

root.mainloop()
