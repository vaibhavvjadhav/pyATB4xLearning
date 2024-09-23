class facebook_login():
    def __init__(self, email_arg, pass_arg):
        self.email = email_arg
        self.password = pass_arg

    def fb_login(self):
        if self.email == 'vvj20032003@yahoo.in' and self.password == 'Shreyansh@143':
            print("Logged In")
        else:
            print("Failed")

email = input("Enter Email")
password = input("Enter Password")

obj = facebook_login(email, password)
obj.fb_login()