"""

 Create a login page backend to ask users to enter the username and password. 
 Make sure to ask for a Re-Type Password and if the password is incorrect give a chance 
 to enter it again but it should not be more than 3 times.

"""

def login_page():

    username = input("Enter username: ")
    password = input("Enter password: ")
    retype_password = input("Re-type password: ")

    attempts = 1
    while password != retype_password:
        if attempts >= 3:
            print("Exceeded 3 attempts. Exiting Now.")
            return False
        print("Passwords do not match. Please re-enter your password.")
        retype_password = input("Re-type password: ")
        attempts += 1

    print("Login Successful!")

login = login_page()

