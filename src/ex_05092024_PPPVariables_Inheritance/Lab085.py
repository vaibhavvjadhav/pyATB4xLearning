class Bank:
    def __init__(self, account_no, balance):
        self.__account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
    def check_balance(self):
        print(self.balance)
    def show_account_no(self, isAuth):
        if isAuth == True:
            print(self.__account_no)
        else:
            print("Not Allowed")

obj = Bank(123123123,100)
obj.deposit(100)
obj.check_balance()
obj.show_account_no(False)
