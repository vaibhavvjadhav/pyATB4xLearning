Marks = int(input("Enter your Marks"))
match Marks:
    case "90 to 100":
        print("Distinction")
    case "80 to 90":
        print("First Class")
    case "70 to 80":
        print("Second Class")
    case _:
        print("Third Class")
