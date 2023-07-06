from tkinter import *

def login():
    username = username_entry.get()
    password = password_entry.get()
    login_type = login_type_var.get()
    
    # Perform login authentication here
    # You can add your own logic to validate the login credentials
    
    if login_type == "Student":
        open_student_page()
    elif login_type == "Instructor":
        open_instructor_page()
    elif login_type == "Admin":
        open_admin_page()

def open_student_page():
    # Create and configure the student page
    student_page = Toplevel(root)
    student_page.attributes('-fullscreen', True)
    
    # Add the student page widgets and functionality here
    
def open_instructor_page():
    # Create and configure the instructor page
    instructor_page = Toplevel(root)
    instructor_page.attributes('-fullscreen', True)
    
    # Add the instructor page widgets and functionality here
    search_label = Label(instructor_page, text="Search Student:")
    search_label.pack()
    search_entry = Entry(instructor_page)
    search_entry.pack()
    search_button = Button(instructor_page, text="Search", command=lambda: search_student(search_entry.get()))
    search_button.pack()
    
def open_admin_page():
    # Create and configure the admin page
    admin_page = Toplevel(root)
    admin_page.attributes('-fullscreen', True)
    
    # Add the admin page widgets and functionality here
    search_label = Label(admin_page, text="Search Student:")
    search_label.pack()
    search_entry = Entry(admin_page)
    search_entry.pack()
    search_button = Button(admin_page, text="Search", command=lambda: search_student(search_entry.get()))
    search_button.pack()

def search_student(student_name):
    # Implement the search functionality here
    # You can add your own logic to search for a student
    
    # Display the search results in a new window or update the existing page

# Create the main window
    root = Tk()
root.attributes('-fullscreen', True)

# Add login page widgets
username_label = Label(root, text="Username:")
username_label.pack()
username_entry = Entry(root)
username_entry.pack()

password_label = Label(root, text="Password:")
password_label.pack()
password_entry = Entry(root, show="*")
password_entry.pack()

login_type_label = Label(root, text="Login Type:")
login_type_label.pack()
login_type_var = StringVar(root)
login_type_var.set("Student")  # Default login type
login_type_dropdown = OptionMenu(root, login_type_var, "Student", "Instructor", "Admin")
login_type_dropdown.pack()

login_button = Button(root, text="Login", command=login)
login_button.pack()

# Run the main event loop
root.mainloop()