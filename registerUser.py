from controller import Controller
from person import Person

class RegisteredUser(Person):
    """! Class RegisteredUser
    it is the child class of the Person class
    inherits parent class attributes and methods
    Registered users can log in and log out of the system
    """
    

    def __init__(self, personName, username, password, email):
        Person.__init__(self, personName)
        """! The initialiser for RegisteredUser
        @param username user name
        @param password users' passwords
        @param email users'emails
        """
        self.username = username
        self.password = password
        self.email = email
        print('This is RegisteredUser class')


     
    def getName(self):
        """! Get registered users names"""
        return self.personName

    def login(self, username:str, password:str, flag:int):
        """! login method allows registered users to login
        @param username usernames for users to login
        @param password password that users can use to login
        """
        
        if Controller.login(username, password, flag) == True:
            print(username + ' login successful')
            return True

        print(username + ' login failed')
        return False

    
    def logout(self, username:str, flag:int):
        """! logout method allows registered users to log out of the system"""
        Controller.logout(username, flag)
        if Controller.logout(username, flag) == True:
            print(username + ' logout successful')
            return True

        print(username + ' logout failed')
        return False

# if __name__ == '__main__':
#     r = RegisteredUser('Shane', 'Shane', 'shane123', 'shane@gmail.com')
#     # r.login('Shane', 'shane123') #ok
#     r.login('Shane', 'shane1234') #failed