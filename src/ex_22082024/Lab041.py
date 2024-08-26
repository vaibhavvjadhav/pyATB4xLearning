usertype = input("Enter the user type: Manager, Admin, Guest")
usertype = usertype.lower()
match usertype:
    case "manager":
        print("Welcome Manager")
    case "admin":
        print("Welcome Admin")
    case "guest":
        print("Welcome Guest")
    case _:
        print("Welcome Unknown")