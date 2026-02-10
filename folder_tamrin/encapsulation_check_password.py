class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def login(self):
        if self.__password == 1234567:
            print(f"login successful!! | Welcome {self.__username} :)")
        else:
            print(f"access denied!! | incorrect password {self.__username} :(")
            
            
            
username = input("enter username: ")

try:
    password = int(input("enter password: "))
except ValueError:
    print("Error: password must be numeric (integer)")
else:
    user = User(username, password)
    user.login()
