# Decorator in python are way to modify the behaviour of a function or class
# without changing its source code
# Decorator is powerful tool that allows you to wrap another function and extend
# its functionality while keeping the original function code unchanged

def my_decorator(func):
    def wrapper():
        print("Before function")
    print("Helmet", "Dashcam", "Knee guard")
    func()
   # ride_bike()
    print("After function")
    print("Drive Safely")
    return wrapper()

@my_decorator
def ride_bike():
    print("Decorator")
