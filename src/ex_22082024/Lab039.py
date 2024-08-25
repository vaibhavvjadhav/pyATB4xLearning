#Match case program

Browser_Name = input("Enter the Browser Name")
#Browser_Name = Browser_Name.title()
match Browser_Name:
    case "FireFox":
        print("Execute the FireFox code")
    case "Chrome":
        print("Execute the Chrome code")
    case "IE":
        print("Execute the IE code")
    case "Edge":
        print("Execute the Edge code")
    case "Safari":
        print("Execute the Safari code")
    case _:
        print("Browser Not Fount!")