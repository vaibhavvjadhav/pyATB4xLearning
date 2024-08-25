# Grade calculator
# A - 90 to 100
# B - 80 to 89
# C - 70 to 79
# D - 60 to 69
# F - 0 to 59

marks_scored = int(input("Enter your marks\n"))
if marks_scored >= 90 and marks_scored <= 100:
    print(f"Your Grade is A : {marks_scored}")
elif marks_scored >= 80 and marks_scored <= 89:
    print(f"Your Grade is B : {marks_scored}")
elif marks_scored >= 70 and marks_scored <= 79:
    print(f"Your Grade is C : {marks_scored}")
elif marks_scored >= 60 and marks_scored <=69:
    print(f"Your Grade is D : {marks_scored}")
elif marks_scored>100:
    print(f"You are Superman : {marks_scored}")
else:
    print(f"You are fail {marks_scored}")
