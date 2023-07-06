import tkinter as tk

def draw_arrow(canvas, x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, arrow="last", fill="black")

def draw_boxes_with_arrows(canvas, boxes):
    box_width = 80
    box_height = 50
    arrow_offset = 10
    arrow_length = 40

    x = 50
    y = 100

    for i in range(len(boxes)-1):
        canvas.create_rectangle(x, y, x + box_width, y + box_height, fill="green")
        draw_arrow(canvas, x + box_width + arrow_offset, y + box_height/2,
                   x + box_width + arrow_offset + arrow_length, y + box_height/2)

        x += box_width + arrow_offset + arrow_length

    canvas.create_rectangle(x, y, x + box_width, y + box_height, fill="green")

root = tk.Tk()
root.title("Degree Audit")

canvas_width = 900
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

# Creating columns for each year
year_columns = []
years = ["2020", "2021", "2022", "2023", "2024"]
semesters = ["Fall", "Spring"]

column_width = (canvas_width - 100) // len(years)
column_height = canvas_height - 100
x_offset = 50
y_offset = 50

for i, year in enumerate(years):
    x = x_offset + i * column_width

    for j, semester in enumerate(semesters):
        y = y_offset + j * column_height
        subheader = f"{year} {semester}"
        canvas.create_text(x + column_width // 2, y + 20, text=subheader, anchor="center")
        canvas.create_rectangle(x, y + 40, x + column_width, y + column_height, fill="white")

        year_columns.append((x, y + 40, x + column_width, y + column_height))

boxes = ["Box 1", "Box 2", "Box 3", "Box 4", "Box 5"]
draw_boxes_with_arrows(canvas, boxes)

root.mainloop()
