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