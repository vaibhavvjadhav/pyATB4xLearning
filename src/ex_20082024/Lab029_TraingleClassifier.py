#Write a program that classifies a triangle based on its side lengths.

#Given three input values representing the lengths of the sides,

#determine if the triangle is equilateral (all sides are equal),

#isosceles (exactly two sides are equal), or scalene (no sides are equal).

#Use an if-else statement to classify the triangle.

a = int(input("Enter the 1 side of triangle"))
b = int(input("Enter the 2 side of triangle"))
c = int(input("Enter the 3 side of triangle"))

if a==b and b==c:
    print(f"Equilateral : {a},{b},{c}")
elif a==b and a!=c:
    print(f"isosceles : {a},{b},{c}")
elif a!=b and b!=c:
    print(f"Scalene : {a},{b},{c}")