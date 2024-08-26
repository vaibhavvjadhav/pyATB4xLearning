year = int(input("Enter the year"))
if year % 4 == 0 and year % 400 == 0:
    print(f"Leap year : {year}")
elif year % 4 == 0 and year % 100 != 0:
    print(f"Not a Leap year :{year}")
else:
    print("Leap year: ", year)

