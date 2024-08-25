x = int(input("Enter value of X"))
y = int(input("Enter value of Y"))
z = int(input("Enter value of Z"))

if x > y and x > z:
    print(f"X is greater {x}")
elif y > x and y > z:
    print(f"Y is greater {y}")
else:
    print(f"Z is greater {z}")

result = max(x, y, z)
print("max is :", result)
