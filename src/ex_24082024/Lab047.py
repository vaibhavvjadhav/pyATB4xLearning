# addition of 3 number using function

num1 = int(input("Enter the number 1:"))
num2 = int(input("Enter the number 2:"))
num3 = int(input("Enter the number 3:"))


def sum_of_numbers(n1, n2, n3):
    return n1 + n2 + n3


result = sum_of_numbers(n1=num1, n2=num2, n3=num3)
print(result)
result = sum_of_numbers(num1, num2, num3)
print(result)
