class Father:
    key = 1
    __password = "private"
    def fathers_money(self):
        return 5
    def __show_password(self):
        print(self.__password)

    def home(self):
        print("Fathers 2BHK")

    def show_everything(self):
        self.__show_password()

class Mother:
    def mothers_money(self):
        return 3

    def home(self):
        print("Mothers 2BHK")

class Son(Father, Mother):
    pass
S = Son()
print(S.fathers_money())
print(S.mothers_money())
print(S.home())
print(S.key)
S.show_everything()
S.show_password()

class Son2(Mother, Father):
    pass


S2 = Son2()
print(S2.home())
print(S2.key)
S2.show_everything()