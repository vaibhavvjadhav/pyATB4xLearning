class Calc():
    def __init__(self):
        print("Calculator")

    def sum(self, a , b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a , b):
        return a * b

    def div(self, a, b):
        return a / b

cal = Calc()
a = int(input("Enter the value of A:"))
b = int(input("Enter the Value of B:"))
calsum = cal.sum(a,b)
print(f"Addition is {calsum}")
calsub = cal.sub(a, b)
print(f"Subrtaction is {calsub}")
calmul = cal.mul(a, b)
print(f"Multiplication is {calmul}")
caldiv = cal.div(a, b)
print(f"Division is {caldiv}")