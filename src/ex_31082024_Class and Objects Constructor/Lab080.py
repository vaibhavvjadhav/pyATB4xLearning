class Calc():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

cal = Calc(3, 4)
output = cal.sum()
print(f"Sum is {output}")
cal1 = Calc(10, 5)
output = cal1.sub()
print(f"Sub is {output}")
cal = Calc(10, 10)
output = cal.mul()
print(f"Mul is {output}")
cal = Calc(10, 5)
output = cal.div()
print(f"Sum is {output}")