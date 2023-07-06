from tkinter import *
import tkinter 
#pip install pillow
from PIL import ImageTk, Image 
from tkinter import PhotoImage, messagebox
import sqlite3


class MainPage(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login") 
        #setting page geometry to the size of the user's screen
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.geometry("%dx%d" % (width_screen, height_screen))
        self.iconphoto(False, PhotoImage(file = 'Images_for_Gui/images.png'))
        self.login_frame = LoginFrame(self)
        self.ShowLoginFrame()


    def ShowLoginFrame(self):
        #setting page geometry to the size of the user's screen
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))



class LoginFrame (tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        
        self.label = tkinter.Label(self, text="Enter Username & Password", font=('Times',14), bg="white")
        self.label.place(x=20, y=40)
        
        self.username_label = tkinter.Label(self, text="Username:", font=('Times',12), bg="white")
        self.username_label.place(x=20, y=80)
        self.username_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.username_entry.place(x=20, y=110)
        
        self.password_label = tkinter.Label(self, text="Password:", font=('Times',12), bg="white")
        self.password_label.place(x=20, y=140)
        self.password_entry = tkinter.Entry(self, show="*", highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.password_entry.place(x=20, y=170)
        
        self.login_button = tkinter.Button(self, text="Login", bg="red", fg="white", width=17, font=('Times',24), bd=0, command=self.login)
        self.login_button.place(x=20, y=210)
    def login(self):
        username = self.username_entry.get() 
        password = self.password_entry.get()

        DbConnect = sqlite3.connect("Database/tables.db")
        db= DbConnect.cursor()      
        db.execute("SELECT 1 FROM AUTHENTIFY  WHERE USERNAME = ? and PASSWORD = ? ", (username, password))
        
        result = db.fetchone()
        index = db.fetchall()

        for row in index:
            print(row)
        
        # Perform login validation here (e.g., check against a database)
        # For simplicity, we'll use a dummy check
        if result:
            if index.Description == "Student":
                self.master.show_home_frame()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def login(self):
        username = self.username_entry.get() 
        password = self.password_entry.get()

        DbConnect = sqlite3.connect("Database/tables.db")
        db= DbConnect.cursor()      
        db.execute("SELECT 1 FROM AUTHENTIFY  WHERE USERNAME = ? and PASSWORD = ? ", (username, password))
        
        result = db.fetchone()
        index = db.fetchall()

        for row in index:
            print(row)
        

class StudentFrame (tkinter.Frame):
     def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        self.label = tkinter.Label(self, text="Main Menu", font=('Times',14), bg="white")
        self.label.place(x=20, y=40)
        
        self.Search_button = tkinter.Button(self, text="Search Courses", bg="red", fg="white", width=17, font=('Times',24), bd=0, command=self.login)
        self.Search_button.place(x=20, y=210)
        
        self.Add_button = tkinter.Button(self, text="Add Courses", bg="red", fg="white", width=17, font=('Times',24), bd=0, command=self.login)
        self.Add_button.place(x=20, y=80)
        
        self.Drop_button = tkinter.Button(self, text="Drop Courses", bg="red", fg="white", width=17, font=('Times',24), bd=0, command=self.login)
        self.Drop_button.place(x=20, y=100)

        self.Print_button = tkinter.Button(self, text="Print Schedule", bg="red", fg="white", width=17, font=('Times',24), bd=0, command=self.login)
        self.Print_button.place(x=20, y=180)

class Print_ScheduleFrame (tkinter.Frame):
     def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
     def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        self.View_button = tkinter.Button(self, text="View Course Schedule", bg="red", fg="white", width=17, font=('Times',24), bd=0, command=self.login)
        self.View_button.place(x=20, y=210)

        self.Print_button = tkinter.Button(self, text="Print your Schedule", bg="red", fg="white", width=17, font=('Times',24), bd=0, command=self.login)
        self.Print_button.place(x=20, y=110)

     def go_back(self):
        self.master.show_home_frame()

        DbConnect = sqlite3.connect("Database/tables.db")
        db= DbConnect.cursor()      
        db.execute("Courses", (courses))
        
        result = db.fetchone()
        index = db.fetchall()

        for row in index:
            print(row)


if __name__ == "__main__":
    app = MainPage()
    app.mainloop()
