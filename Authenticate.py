#Collin Paquin - Version 62123.546
import sqlite3

# Establishing a connection to the SQLite database
connection = sqlite3.connect("DegreeViz.db")
cursor = connection.cursor()

# Function to check access
def check_access(email, password):
    query = "SELECT Password FROM Users WHERE Email = ?"
    cursor.execute(query, (email,))
    result = cursor.fetchone()

    if result and result[0].strip() == password:
        print("Access Granted")
        user_type = input("Enter your user type (S for Student, P for Professor, A for Admin): ")
        
        if user_type == "S":
            print("Welcome, Student!")
            display_degree_audit = input("Do you want to display a new Degree Audit? (Y/N): ")
            if display_degree_audit == "Y":
                print("Displaying new Degree Audit...")

        elif user_type == "P":
            print("Welcome, Professor!")
            professor_options = input("Professor options: \n1. Display a student's degree audit\n2. Update grades\nChoose an option (1/2): ")
            if professor_options == "1":
                print("Displaying a student's degree audit...")
            elif professor_options == "2":
                print("Updating grades...")
            else:
                print("Invalid option.")
            
        elif user_type == "A":
            print("Welcome, Admin!")
            admin_options = input("Admin options: \n1. Update grades\n2. Add or remove classes\n3. Assign a professor to a class\nChoose an option (1/2/3): ")
            if admin_options == "1":
                print("Updating grades...")
            elif admin_options == "2":
                print("Adding or removing classes...")
            elif admin_options == "3":
                print("Assigning a professor to a class...")
            else:
                print("Invalid option.")
            
        else:
            print("Invalid user type.")
    else:
        print("Access Denied")

# Getting input from the user
user_email = input("Enter your email: ")
user_password = input("Enter your password: ")

# Checking access
check_access(user_email, user_password)

# Closing the cursor and connection
cursor.close()
connection.close()
