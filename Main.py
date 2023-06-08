# Ricardo Moreira, Tory Curro, Santino Nardolillo, Liam Nasr, Collin Paquin, Tommaso Verdiglione
# ELEC 3225
# Visualizing the Degree Audit

# Creation of Parent Class (User)
class User:

    #constructor
    def __init__(self, first_name, last_name , ID):
        self.first_name = first_name
        self.last_name = last_name
        self.ID = ID

    def first_name(self, first_name):
        print("First Name: ", self.first_name)

    def last_name(self, last_name):
        print("Last Name: ", self.last_name)

    def ID(self, ID):
        print("ID: ", self.ID)

    def intro(self):
        print("Full Name: ", self.first_name, self.last_name)
        print("ID: ", self.ID)

# Creation of Child Class (Student)
class Student(User):
    def searchcourses(self):
        print("SEARCH FOR COURSES FUNCTION COMPLETE")

    def adddrop(self):
        print("ADD/ DROP COURSES FUNCTION COMPLETE")

    def schedule(self):
        print("PRINT SCHEDULE FUNCTION COMPLETE")

# Creation of Child Class (Instructor)
class Instructor(User):
    def schedule(self):
        print("PRINT SCHEDULE FUNCTION COMPLETE")

    def classlist(self):
        print("PRINT CLASS LIST FUNCTION COMPLETE")

    def searchcourses(self):
        print("SEARCH FOR COURSES FUNCTION COMPLETE")

# Creation of Child Class (Admin)
class Admin(User):
    def addcoursessystem(self):
        print("ADD COURSES FUNCTION COMPLETE")

    def removecoursessystem(self):
        print("REMOVE COURSES FUNCTION COMPLETE")

    def addremoveusers(self):
        print("ADD/ REMOVE USERS FUNCTION COMPLETE")

    def addremovestudents(self):
        print("ADD/ REMOVE STUDENTS FUNCTION COMPLETE")

    def searchrosters(self):
        print("SEARCH FOR ROSTERS FUNCTION COMPLETE")
        
    def searchcourses(self):
        print("SEARCH FOR COURSES FUNCTION COMPLETE")

# User Demonstration
student1 = User("Santino", "Nardolillo", "114")
student1.intro()
print()

# Student Demonstration
student3 = Student("John", "Doe", "123")
student3.intro()
student3.searchcourses()
student3.adddrop()
student3.schedule()
print()

# Instructor Demonstration
student4 = Instructor("Jeremy", "Smith", "456")
student4.intro()
student4.schedule()
student4.classlist()
student4.searchcourses()
print()

# Admin Demonstration
student2 = Admin("Jim", "Joe", "654")
student2.intro()
student2.addcoursessystem()
student2.removecoursessystem()
student2.addremoveusers()
student2.addremovestudents()
student2.searchrosters()
student2.searchcourses()
print()