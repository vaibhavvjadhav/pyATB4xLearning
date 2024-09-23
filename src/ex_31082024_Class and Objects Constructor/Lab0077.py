class Dog:
    name = None

    def sleep(self):
        print("Sleeping")
    def __init__(self, name):
        print("I will be automatically called when you create object")
        print("called, object is created")
        self.name = name

D1 = Dog("Tiger")
print(D1.name)
