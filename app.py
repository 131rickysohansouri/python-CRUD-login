from dbhelper import DBhelper
import sys
class Flipkart:
    def __init__(self):
        #Connect to the database
        self.db=DBhelper()
        self.menu()

    def menu(self):
        user_input=input("""
        1.Enter 1 to register 
        2.Enter 2 to login
        3.Anything else to leave """)

        if user_input =="1":
            self.register()

        elif user_input == "2":
            self.login()
        
        else:
            sys.exit(1000)

    def login_menu(self):
        user_input=input("""
        1.Enter 1 to see profile
        2.Enter 2 to edit profile
        3.Anything else to logout """)


    def register(self):
        name=input("Enter your name")
        email=input("Enter your email")
        password=input("Enter your password")
        response=self.db.register(name,email,password)
        if response:
            print("Registration Successful")
        else:
            print("Try again")

    def login(self):
        email=input("Enter your email")
        password=input("Enter your password")
        data=self.db.search(email,password)

        if len(data)== 0:
            print("Incorrect Credentials")
            self.login()

        else:
            print("Hello",data[0][1])

        
    
obj= Flipkart()
