class vmologin():

    def __init__(self, username_arg, pass_arg):
        self.username = username_arg
        self.password = pass_arg

    def login(self):
        if self.username == 'vaibhavvijayjadhav@gmail.com' and self.password == 'Devansh@2020':
            print("Login Successfully")
        else:
            print("Login Failed")

username = input("Enter the username")
password = input("Enter the Password")
obj = vmologin(username, password)
obj.login()
