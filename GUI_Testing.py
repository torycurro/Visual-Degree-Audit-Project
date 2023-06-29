import tkinter as tk
from tkinter import PhotoImage, messagebox
import sqlite3


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login System")
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.geometry("%dx%d" % (width_screen, height_screen))
        self.iconphoto(False, PhotoImage(file = 'Images_for_Gui/images.png'))
        self.login_frame = LoginFrame(self)
        self.home_frame = HomeFrame(self)
        self.profile_frame = ProfileFrame(self)
        
        self.show_login_frame()
        
    def show_login_frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.home_frame.pack_forget()
        self.profile_frame.pack_forget()
        
    def show_home_frame(self):
        self.login_frame.pack_forget()
        self.home_frame.pack()
        self.profile_frame.pack_forget()
        
    def show_profile_frame(self):
        self.login_frame.pack_forget()
        self.home_frame.pack_forget()
        self.profile_frame.pack()
        

class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        
        self.label = tk.Label(self, text="Enter Username & Password", font=('Times',14), bg="white")
        self.label.place(x=20, y=40)
        
        self.username_label = tk.Label(self, text="Username:", font=('Times',12), bg="white")
        self.username_label.place(x=20, y=80)
        self.username_entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.username_entry.place(x=20, y=110)
        
        self.password_label = tk.Label(self, text="Password:", font=('Times',12), bg="white")
        self.password_label.place(x=20, y=140)
        self.password_entry = tk.Entry(self, show="*", highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.password_entry.place(x=20, y=170)
        
        self.login_button = tk.Button(self, text="Login", bg="red", fg="white", width=17, font=('Times',24), bd=0, command=self.login)
        self.login_button.place(x=20, y=210)
        
    def login(self):
        username = self.username_entry.get() 
        password = self.password_entry.get()
        
        DbConnect = sqlite3.connect("DegreeViz.db")
        db = DbConnect.cursor()
        db.execute("SELECT 1 FROM Users  WHERE Email = ? and Password = ? ", (username, password))
        result = db.fetchone()
        if result:
            for column in db.execute("SELECT * FROM Users WHERE Email = ? and Password = ? ", (username, password)):
                if  result:
                    if column[5] == 'S':
                        self.master.show_home_frame()
                    else:
                        messagebox.showerror("Login Failed", "Invalid username or password.")                   
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.") 
             

        # Perform login validation here (e.g., check against a database)
        # For simplicity, we'll use a dummy check
        


class HomeFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, )
        
        self.label = tk.Label(self, text="Home Page")
        self.label.pack(pady=10)
        
        self.profile_button = tk.Button(self, text="View Profile", command=self.view_profile)
        self.profile_button.pack(pady=5)
        
        self.logout_button = tk.Button(self, text="Logout", command=self.logout)
        self.logout_button.pack(pady=5)
        
    def view_profile(self):
        self.master.show_profile_frame()
        
    def logout(self):
        self.master.show_login_frame()


class ProfileFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label = tk.Label(self, text="Profile Page")
        self.label.pack(pady=10)
        
        self.back_button = tk.Button(self, text="Back", command=self.go_back)
        self.back_button.pack(pady=5)
        
    def go_back(self):
        self.master.show_home_frame()


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()