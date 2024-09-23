a = 10 #global variable

class globalinstance():
    b = 11 #instance Variable

    def declarevariable(self):
        global a # global declaration with in class with global keyword
        a = 200
        print(a)
        print(self.b) # b should be declared as self

GI = globalinstance()
GI.declarevariable()