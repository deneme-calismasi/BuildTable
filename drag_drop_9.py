import tkinter as tk
import numpy as np
from PIL import Image, ImageTk

# drag callbacks
dragged_item = None
current_coords = 0, 0


def start_drag(event):
    global current_coords
    global dragged_item
    result = canvas.find_withtag('current')
    if result:
        dragged_item = result[0]
        current_coords = canvas.canvasx(event.x), canvas.canvasy(event.y)
    else:
        dragged_item = None


def stop_drag(event):
    dragged_item = None


def drag(event):
    global current_coords
    xc, yc = canvas.canvasx(event.x), canvas.canvasy(event.y)
    dx, dy = xc - current_coords[0], yc - current_coords[1]
    current_coords = xc, yc
    canvas.move(dragged_item, dx, dy)


# Create pictures
blue_square_transparent_border = [[[0, 0, 0, 0]] * 100] * 10 + [
    [[0, 0, 0, 0]] * 30 + [[0, 0, 255, 255]] * 40 + [[0, 0, 0, 0]] * 30] * 40 + [[[0, 0, 0, 0]] * 100] * 10
blue_square_transparent_border = np.array(blue_square_transparent_border, dtype='uint8')
pil_image = Image.fromarray(blue_square_transparent_border)

background_data = np.zeros((200, 400, 4))
background_data[:, :, 0] = 255 * np.ones((200, 400))
background_data[:, :, 3] = 255 * np.ones((200, 400))
background_data = np.array(background_data, dtype='uint8')
pil_image_bg = Image.fromarray(background_data)

# create GUI
root = tk.Tk()
background_image = ImageTk.PhotoImage(pil_image_bg)
tk_image = ImageTk.PhotoImage(pil_image)

canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()
# bind 'draggable' tag to mouse events
canvas.tag_bind('draggable', '<ButtonPress-1>', start_drag)
canvas.tag_bind('draggable', '<ButtonRelease-1>', stop_drag)
canvas.tag_bind('draggable', '<B1-Motion>', drag)
# display pictures
canvas.create_image(0, 0, image=background_image, anchor='nw')
canvas.create_image(0, 0, image=tk_image, anchor='nw', tag='draggable')

root.mainloop()
