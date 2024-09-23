class Employee:
    name = None
    age = None
    phone = None
    address = None
    eid = None

    n = input("Enter the Emplyee name")
    a = input("Enter the Age:")
    p = input("Enter phone no")
    ad = input("Enter the address")
    e = input("Enter the employee id")

    def __init__(self, name, age, phone, address, eid):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.eid = eid

    def walk(self):
        print("Employee is walking")

    def talk(self):
        print("Ëmployee is talking")


E1 = Employee(name=n, age=a, phone=p, address=ad, eid=e)
#E1.name
E1.walk()
print(E1.name, E1.age, E1.phone, E1.address, E1.eid)
