class parent:
    gold = "2KGS"

    def bhk3(self):
        print("3BHK")

class Child(parent):
    def bhk2(self):
        print("2BHK")

obj1 = Child()
print(obj1.gold)
obj1.bhk3()
obj1.bhk2()



