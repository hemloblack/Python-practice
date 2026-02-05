class websit:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        if len(password) < 8:
            print("error: password must be at least 8 characters")

    def len_pass(self):
        return len(self.password)

    def change(self, new_password):
        if new_password == self.password or len(new_password) < 8:
            print("error: change")
        else:
            self.password = new_password
            print("update password")

    def show_info(self):
        passwordstar = "*" * self.len_pass()
        print(f"hello im {self.username} my password in website {passwordstar}")
        
user1 = websit("ali", "2211")
user1.show_info()
