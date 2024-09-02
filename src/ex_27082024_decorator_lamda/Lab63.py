def new_decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()

    return wrapper()


def new_decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()

    return wrapper()


@new_decorator1
@new_decorator2
def testfunc():
    print("Test")


testfunc()



