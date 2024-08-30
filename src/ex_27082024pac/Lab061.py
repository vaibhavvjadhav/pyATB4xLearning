def my_decorator(func):
    def wrapper():
        print("Before function call")
        print("Add Helmet, Sunglasses, knee guard, shoes")
        func()
        print("After function call")
        print("Drive safely")

        return wrapper()


@my_decorator
def drive_bike():
    print("I am driving")
