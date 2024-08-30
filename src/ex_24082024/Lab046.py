# No return type
def greet():
    print("Hello")


greet()


# No return type with argument
def greet_by_name(name):
    print("Hello,", name)


greet_by_name("Vaibhav")


# No return type with default argument

def greet_by_default_arg(name='Vaibhav'):
    print("Welcome,", name)


greet_by_default_arg('Amol')
greet_by_default_arg()  # No value pass it will take default arg i.e Vaibhav
greet_by_default_arg(name='Jadhav')  # Positional argument


# Multiple arguments
def multiple_args(name='Shreyansh', name1='Devansh', name2='Vaibhav'):
    print("Hey,", name, name1, name2)


multiple_args()
multiple_args('Vaibhav', 'Vijay', 'Jadhav')


# Argument with return

def sum_of_two_nums(num1, num2):
    return num1 + num2


result = sum_of_two_nums(10, 20)
print(result)
