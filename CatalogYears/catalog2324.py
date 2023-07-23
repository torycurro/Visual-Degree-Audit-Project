import tkinter as tk
import sqlite3

def draw_degree_audit2324(wnumber, studentname):
    def draw_arrow(canvas, x1, y1, x2, y2):
        canvas.create_line(x1, y1, x2, y2, arrow="last", fill="black")

    def draw_boxes_with_arrows(canvas, boxes):
        box_width = 70
        box_height = 40
        arrow_offset = 10
        arrow_length = 20

        x = 50
        y = 100
        yfall = 100
        xfall = 60
        yspring = 100
        xspring = 190
        xSfall = 410
        ySfall = 100
        xSspring = 530
        ySspring = 100
        xSsummer = 640
        ySsummer = 100
        xJfall = 780
        yJfall = 100
        xJspring = 890
        yJspring = 100
        xJsummer = 990
        yJsummer = 100
        xSNfall = 1100
        ySNfall = 100
        xSNspring = 1230
        ySNspring = 100
        xSNsummer = 1350
        ySNsummer = 100

        def grade(coursename,studentWnumber):
            Dbconnect = sqlite3.connect("Database/DegreeViz-2R4.db")
            db = Dbconnect.cursor() 
            course = coursename
            courseGrade = " "
            for data in db.execute("SELECT * From Grades Where Course = ? and Wnumber = ? ",(str(course), studentWnumber)):
               courseGrade = int(data[2])                   
            if courseGrade >= 90:
               return "green"
            elif courseGrade >= 80 and courseGrade <= 89:
               return "blue"
            elif courseGrade >= 70 and courseGrade <= 79:
                return "yellow"
            elif courseGrade >= 64 and courseGrade <=69:
                return "orange"
            elif courseGrade < 64 :
                return "red"
            else:
              return "white"
            db.close()
                   
        def convert_tup_str(data):
            coursename = ""
            for item in data:
               coursename = coursename + item
            return coursename

        for i in range(len(boxes)):
            if i < 5:
                fillCollor = grade(convert_tup_str(boxes[i]),wnumber)
                canvas.create_rectangle(xfall, yfall, xfall + box_width, yfall + box_height, fill=fillCollor)
                text_x = xfall + box_width / 2 
                canvas.create_text(text_x, yfall + box_height / 2, text=boxes[i], anchor="center")
                yfall += 50
            elif (i>=5 and i<10):
                fillCollor = grade(convert_tup_str(boxes[i]),wnumber)
                canvas.create_rectangle(xspring, yspring, xspring + box_width, yspring + box_height, fill=fillCollor)
                text_x = xspring +box_width / 2  
                canvas.create_text(text_x, yspring + box_height / 2, text=boxes[i], anchor="center")
                yspring += 50
            elif (i>=10 and i<13):
                fillCollor = grade(convert_tup_str(boxes[i]),wnumber)
                canvas.create_rectangle(xSfall, ySfall, xSfall + box_width, ySfall + box_height, fill=fillCollor)
                text_x = xSfall +box_width / 2  
                canvas.create_text(text_x, ySfall + box_height / 2, text=boxes[i], anchor="center")
                ySfall += 50
            elif (i>=13 and i<17):
                fillCollor = grade(convert_tup_str(boxes[i]),wnumber)
                canvas.create_rectangle( xSspring, ySspring,  xSspring + box_width, ySspring + box_height, fill=fillCollor)
                text_x =  xSspring +box_width / 2  
                canvas.create_text(text_x, ySspring + box_height / 2, text=boxes[i], anchor="center")
                ySspring += 50
            elif (i>=17 and i<20):
                fillCollor = grade(convert_tup_str(boxes[i]),wnumber)
                canvas.create_rectangle( xJfall, yJfall,  xJfall + box_width, yJfall + box_height, fill=fillCollor)
                text_x =  xJfall +box_width / 2  
                canvas.create_text(text_x, yJfall + box_height / 2, text=boxes[i], anchor="center")
                yJfall += 50
            elif (i>=20 and i<24):
                fillCollor = grade(convert_tup_str(boxes[i]),wnumber)
                canvas.create_rectangle( xJsummer, yJsummer,  xJsummer + box_width, yJsummer + box_height, fill=fillCollor)
                text_x =  xJsummer +box_width / 2  
                canvas.create_text(text_x, yJsummer + box_height / 2, text=boxes[i], anchor="center")
                yJsummer += 50
            elif (i>=24 and i<27):
                fillCollor = grade(convert_tup_str(boxes[i]),wnumber)
                canvas.create_rectangle( xSNspring, ySNspring,  xSNspring + box_width, ySNspring + box_height, fill=fillCollor)
                text_x =  xSNspring +box_width / 2  
                canvas.create_text(text_x, ySNspring + box_height / 2, text=boxes[i], anchor="center")
                ySNspring += 50
            elif (i>=27 and i<29):
                fillCollor = grade(convert_tup_str(boxes[i]),wnumber)
                canvas.create_rectangle( xSNsummer, ySNsummer,  xSNsummer + box_width, ySNsummer + box_height, fill=fillCollor)
                text_x =  xSNsummer +box_width / 2  
                canvas.create_text(text_x, ySNsummer + box_height / 2, text=boxes[i], anchor="center")
                ySNsummer += 50
            elif (i==29):
                fillCollor = grade(convert_tup_str(boxes[i]),wnumber)
                canvas.create_rectangle( xSsummer, ySsummer,  xSsummer + box_width, ySsummer + box_height, fill=fillCollor)
                text_x =  xSsummer +box_width / 2  
                canvas.create_text(text_x, ySsummer + box_height / 2, text=boxes[i], anchor="center")
                ySsummer += 50
            elif (i==30):
                fillCollor = grade(convert_tup_str(boxes[i]),wnumber)
                canvas.create_rectangle( xJspring, yJspring,  xJspring + box_width, yJspring + box_height, fill=fillCollor)
                text_x =  xJspring +box_width / 2  
                canvas.create_text(text_x, yJspring + box_height / 2, text=boxes[i], anchor="center")
                yJspring += 50
            elif (i==31):
                fillCollor = grade(convert_tup_str(boxes[i]),wnumber)
                canvas.create_rectangle( xSNfall, ySNfall,  xSNfall + box_width, ySNfall + box_height, fill=fillCollor)
                text_x =  xSNfall +box_width / 2  
                canvas.create_text(text_x, ySNfall + box_height / 2, text=boxes[i], anchor="center")
                ySNfall += 50
            


    root = tk.Tk()
    root.title(f"Degree Audit - {wnumber} - {studentname}")

    canvas_width = 1500
    canvas_height = 400
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
    canvas.pack()

    # Creating columns for each year
    year_columns = []



    years = ["Freshman", "Sophmore", "Junior", "Senior"]
    semesters = ["Fall", "Spring", "Summer"]

    column_width = (canvas_width - 100) // (len(years) * len(semesters))
    column_height = canvas_height - 100
    x_offset = 50
    y_offset = 50

    for i, year in enumerate(years):
        for j, semester in enumerate(semesters):
            x = x_offset + (i * len(semesters) + j) * column_width
            y = y_offset
            subheader = f"{year} {semester}"
            canvas.create_text(x + column_width // 2, y + 20, text=subheader, anchor="center")
            canvas.create_rectangle(x, y + 40, x + column_width, y + column_height, fill="white")

            year_columns.append((x, y + 40, x + column_width, y + column_height))

        

    # For demonstration purposes, I'll use a predefined list of courses.
    # Replace this with the actual data you have for the student.

    Dbconnect = sqlite3.connect("Database/DegreeViz-2R4.db")

    db = Dbconnect.cursor()

    course=[]
    
    db.execute("SELECT CourseCode From Courses2324 ORDER BY rowid")
    data= db.fetchall()
   
    draw_boxes_with_arrows(canvas, data)
    db.close()
    if __name__ == "__main__":
        root.mainloop()


    
