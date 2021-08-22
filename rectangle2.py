from tkinter import *

root = Tk()
root.title("Bar Graph")

c_width = 500
c_height = 200
c_rect = Canvas(root, width=c_width, height=c_height)
c_rect.pack()

c_rect.create_rectangle(20, 140, 120, 180, fill="red")
c_rect.create_text(70, 130, text="Projects--20%")
c_rect.create_rectangle(140, 160, 240, 180, fill="blue")
c_rect.create_text(190, 150, text="Quizzes--10%")
c_rect.create_rectangle(260, 120, 360, 180, fill="green")
c_rect.create_text(310, 110, text="Midterm--30%")
c_rect.create_rectangle(380, 100, 480, 180, fill="orange")
c_rect.create_text(430, 90, text="Final--40%")
c_rect.create_line(0, 180, 500, 180)

root.mainloop()
