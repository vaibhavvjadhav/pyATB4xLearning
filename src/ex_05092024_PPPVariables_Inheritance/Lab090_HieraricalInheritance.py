class Father:
    def bhk3(self):
        print("3BHK")

class Vaibhav(Father):
    def bhk2(self):
        print("2BHK")

class Santosh(Father):
    def bhk1(self):
        print("1BHK")

class Dipti(Father):
    def noHome(self):
        print("no home")


D = Dipti()
D.bhk3()
D.noHome()

S = Santosh()
S.bhk3()
S.bhk1()

V = Vaibhav()
V.bhk3()
V.bhk2()