class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Error: amount must be positive")
        else:
            self.__balance += amount

    def show(self):
        print(f"The balance is {self.__balance}")
balancing = BankAccount(2500)
balancing.deposit(1000)
balancing.show()
