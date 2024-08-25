# pi either math.pi or pi=3.14
# radius - user input
import math

radius = float(input("Enter the radius of circle"))
area_of_circle = (math.pi * (radius ** 2))
area_of_circle2 = math.pi * pow(radius, 2)
area_of_circle3 = 3.14 * pow(radius, 2)
print("Area of circle 1 :",area_of_circle)
print("Area of circle 2:" f"{area_of_circle2:.2f}")
print("Area of circle 3:" f"{area_of_circle3:.4f}")

