import sqlite3

# Establishing a connection to the SQLite database
connection = sqlite3.connect("DegreeViz-2R2.db")
cursor = connection.cursor()

class User:
    def __init__(self, wnumber, email, password, last_name, first_name):
        self.wnumber = wnumber
        self.email = email
        self.password = password
        self.last_name = last_name
        self.first_name = first_name

    def display_user_info(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Wnumber: {self.wnumber}")
        print(f"Email: {self.email}")

class Student(User):
    def __init__(self, wnumber, email, password, last_name, first_name, catalog_year):
        super().__init__(wnumber, email, password, last_name, first_name)
        self.catalog_year = catalog_year

    def display_student_info(self):
        self.display_user_info()
        print(f"Catalog Year: {self.catalog_year}")

    def display_degree_audit(self):
        print("Displaying new Degree Audit...")

class Professor(User):
    def __init__(self, wnumber, email, password, last_name, first_name):
        super().__init__(wnumber, email, password, last_name, first_name)

    def display_professor_info(self):
        self.display_user_info()

    def display_student_degree_audit(self, student):
        student.display_degree_audit()

class Admin(User):
    def __init__(self, wnumber, email, password, last_name, first_name):
        super().__init__(wnumber, email, password, last_name, first_name)

    def display_admin_info(self):
        self.display_user_info()


# Function to check access
def check_access(email, password):
    query = "SELECT UserType, Wnumber, LastName, FirstName, CatalogYear FROM Users WHERE Email = ? AND Password = ?"
    cursor.execute(query, (email, password))
    result = cursor.fetchone()

    if result:
        user_type, wnumber, last_name, first_name, catalog_year = result
        print("Access Granted")

        if user_type == "S":
            student = Student(wnumber, email, password, last_name, first_name, catalog_year)
            student.display_student_info()
            display_degree_audit = input("Do you want to display a new Degree Audit? (Y/N): ")
            if display_degree_audit == "Y":
                student.display_degree_audit()

            # Perform student-related actions here

        elif user_type == "P":
            professor = Professor(wnumber, email, password, last_name, first_name)
            professor.display_professor_info()
            professor_options = input(
                "Professor options: \n1. Display a student's degree audit\n2. Update grades\nChoose an option (1/2): ")
            if professor_options == "1":
                student_wnumber = input("Enter the student's Wnumber: ")
                query = "SELECT Email, Password, LastName, FirstName FROM Users WHERE Wnumber = ?"
                cursor.execute(query, (student_wnumber,))
                student_result = cursor.fetchone()
                if student_result:
                    student_email, student_password, student_last_name, student_first_name = student_result
                    student = Student(student_wnumber, student_email, student_password, student_last_name, student_first_name, 0)
                    professor.display_student_degree_audit(student)
                else:
                    print("Student not found.")
            elif professor_options == "2":
                print("Updating grades...")
            else:
                print("Invalid option.")

            # Perform professor-related actions here

        elif user_type == "A":
            admin = Admin(wnumber, email, password, last_name, first_name)
            admin.display_admin_info()
            admin_options = input(
                "Admin options: \n1. Update grades\n2. Add or remove classes\n3. Assign a professor to a class\nChoose an option (1/2/3): ")
            if admin_options == "1":
                print("Updating grades...")
            elif admin_options == "2":
                print("Adding or removing classes...")
            elif admin_options == "3":
                print("Assigning a professor to a class...")
            else:
                print("Invalid option.")

            # Perform admin-related actions here

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
