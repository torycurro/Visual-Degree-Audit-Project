# Ricardo Moreira, Tory Curro, Santino Nardolillo, Liam Nasr, Collin Paquin, Tommaso Verdiglione
# ELEC 3225
# Visualizing the Degree Audit

# Creation of Parent Class (User)
class User: # TC: this is the intro

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
    def displayflow_student1(self):
        print("display the first students flow chart")
    def displayflow_student2(self):
        print("display the second students flow chart")
    def displayflow_student3(self):
        print("display the third students flow chart ")
    def displayflow_student4(self):
        print("display the fouth students flow chart ")
    def displayflow_student5(self):
        print("display the fifth students flow chart ")
    def displayflow_student6(self):
        print("display the sixth students flow chart ")
    def displayflow_student7(self):
        print("display the seventh students flow chart ")
    def displayflow_student8(self):
        print("display the 8th students flow chart ")
    def displayflow_student9(self):
        print("display the ninth students flow chart ")
    def displayflow_student10(self):
        print("display the tenth students flow chart ")
    def add_class(self):
        print("Here they can add a class")
    def delete_class(self):
        print("Here they can delete a class")

# Creation of Child Class (Instructor)
class Instructor(User):
    def displayflow_student1(self):
        print("display the first students flow chart")
    def displayflow_student2(self):
        print("display the second students flow chart")
    def displayflow_student3(self):
        print("display the third students flow chart ")
    def displayflow_student4(self):
        print("display the fouth students flow chart ")
    def displayflow_student5(self):
        print("display the fifth students flow chart ")
    def displayflow_student6(self):
        print("display the sixth students flow chart ")
    def displayflow_student7(self):
        print("display the seventh students flow chart ")
    def displayflow_student8(self):
        print("display the 8th students flow chart ")
    def displayflow_student9(self):
        print("display the ninth students flow chart ")
    def displayflow_student10(self):
        print("display the tenth students flow chart ")

# Creation of Child Class (Admin)
class Admin(User):
    def displayflow_student1(self):
        print("display the first students flow chart")
    def displayflow_student2(self):
        print("display the second students flow chart")
    def displayflow_student3(self):
        print("display the third students flow chart ")
    def displayflow_student4(self):
        print("display the fouth students flow chart ")
    def displayflow_student5(self):
        print("display the fifth students flow chart ")
    def displayflow_student6(self):
        print("display the sixth students flow chart ")
    def displayflow_student7(self):
        print("display the seventh students flow chart ")
    def displayflow_student8(self):
        print("display the 8th students flow chart ")
    def displayflow_student9(self):
        print("display the ninth students flow chart ")
    def displayflow_student10(self):
        print("display the tenth students flow chart ")
    def add_class(self):
        print("Here they can add a class")
    def delete_class(self):
        print("Here they can delete a class")
    
    # be able to change 

# User Demonstration
student1 = User("Santino", "Nardolillo", "114")
student1.intro()
print()

# Admin Demonstration
adminuser = Admin("Jim", "Joe", "654") #make dean
#dont display just change  (dean, academic cordinator, etc. ) be able to change the pre-req the arrow will be deleted 
adminuser.intro()
adminuser.displayflow_student1()
adminuser.displayflow_student2()
adminuser.displayflow_student3()
adminuser.displayflow_student4()
adminuser.displayflow_student5()
adminuser.displayflow_student6()
adminuser.displayflow_student7()
adminuser.displayflow_student8()
adminuser.displayflow_student9()
adminuser.displayflow_student10()
adminuser.add_class()
adminuser.delete_class()
print() 

# Student Demonstration
studentuser = Student("John", "Doe", "123")
studentuser.intro()
studentuser.displayflow_student1()
studentuser.displayflow_student2()
studentuser.displayflow_student3()
studentuser.displayflow_student4()
studentuser.displayflow_student5()
studentuser.displayflow_student6()
studentuser.displayflow_student7()
studentuser.displayflow_student8()
studentuser.displayflow_student9()
studentuser.displayflow_student10()
studentuser.add_class()
studentuser.delete_class()
print()

# Instructor Demonstration
#just view 
instructoruser = Instructor("Jeremy", "Smith", "456")
instructoruser.displayflow_student1()
instructoruser.displayflow_student2()
instructoruser.displayflow_student3()
instructoruser.displayflow_student4()
instructoruser.displayflow_student5()
instructoruser.displayflow_student6()
instructoruser.displayflow_student7()
instructoruser.displayflow_student8()
instructoruser.displayflow_student9()
instructoruser.displayflow_student10()
print()

# PROMPTING USERNAME AND PASSWORD
print("---LOGIN SCREEN---")
username = print("Username: ")
password = print("Password: ")

# IF USERNAME DOES NOT EXIST
print ("TEST: Username does not exist. Please try again.")
print()

# IF PASSWORD IS INCORRECT
print ("TEST: Password is incorrect. Please try again.")
print()