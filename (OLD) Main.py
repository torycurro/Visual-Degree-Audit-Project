import sqlite3

def create_students_table():
    # Connect to the database
    conn = sqlite3.connect('Student.db')
    cursor = conn.cursor()

    # Create the Students table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            StudentID INTEGER PRIMARY KEY,
            First_Name TEXT,
            Last_Name TEXT,
            Email TEXT,
            Major TEXT,
            Wnumber INTEGER,
            Password TEXT
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def add_student():
    # Connect to the database
    conn = sqlite3.connect('Student.db')
    cursor = conn.cursor()

    # Get student information from user input
    First_Name = input("Enter students First Name: ")
    Last_Name = input("Enter students Last Name: ")
    Email = input("Enter students Email: ")
    Major = input("Enter students Major: ")
    wnumber = input("Enter W number: ")
    password = input("Enter password: ")

    # Insert the student into the Students table
    cursor.execute('''
        INSERT INTO Students (First_Name, Last_Name, Email, Major, Wnumber, Password)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (First_Name, Last_Name, Email, Major, wnumber, password))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def remove_student():
    # Connect to the database
    conn = sqlite3.connect('Student.db')
    cursor = conn.cursor()

    # Get the W number of the student to be removed
    wnumber = input("Enter the W number of the student to remove: ")

    # Remove the student from the Students table
    cursor.execute('''
        DELETE FROM Students WHERE Wnumber = ?
    ''', (wnumber,))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Call the function to create the Students table
create_students_table()

# Prompt the student to add themselves to the database
add_student()
remove_student()
