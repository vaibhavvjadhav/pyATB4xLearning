num1 = int(input("Enter number1 \n"))
num2 = int(input("Enter number2 \n"))

calculate = input("Please choose add, sub, mul, div \n")

match calculate:
    case add():
        def sum(num1,num2):
            return num1+num2

        result = sum(num1,num2)

    case sub():