Marks = int(input("Enter your Marks"))
match Marks:
    case 90 | 100:
        if Marks > 90 and Marks < 100:
            print("Distinction")
    case 80 | 90:
       # elif Marks > 80 and Marks < 90:
        print("First Class")
    case 70 | 80:
        # elif (Marks > 70 and Marks < 80):
        print("Second Class")
    case _:
        print("Third Class")
