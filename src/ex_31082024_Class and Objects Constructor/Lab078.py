class employee:

    def __init__(self):
        self.name = input(f"Enter the name \n")
        self.age = input(f"Enter the age \n")
        self.gender = input("Enter the Gender \n")
        self.eid = input("Enter the Employee Id")

    def employee_information(self):
        print(f"Employee Name is {self.name}")
        print(f"Employee Age is {self.age}")
        print(f"Employee Gender is {self.gender}")
        print(f"Employee Id is {self.eid}")

emp = employee()
emp.employee_information()
