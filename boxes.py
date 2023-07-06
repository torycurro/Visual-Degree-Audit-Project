import tkinter as tk

def draw_arrow(canvas, x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, arrow="last", fill="black")

def draw_boxes_with_arrows(canvas, boxes):
    box_width = 80
    box_height = 50
    arrow_offset = 10
    arrow_length = 40

    x = 50
    y = 50

    for i in range(len(boxes)-1):
        canvas.create_rectangle(x, y, x + box_width, y + box_height, fill="green")
        draw_arrow(canvas, x + box_width + arrow_offset, y + box_height/2,
                   x + box_width + arrow_offset + arrow_length, y + box_height/2)

        x += box_width + arrow_offset + arrow_length

    canvas.create_rectangle(x, y, x + box_width, y + box_height, fill="green")

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=200)
canvas.pack()

boxes = ["Box 1", "Box 2", "Box 3", "Box 4", "Box 5"]
draw_boxes_with_arrows(canvas, boxes)

root.mainloop()
