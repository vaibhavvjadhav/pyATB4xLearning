class father:
    key = "3BHK"

    def car(self):
        print("Father drives","PADMINI", f",and have {self.key}") #self.key refers to instance varaible

class son(father):
    pass

father_obj = father()
father_obj.car()
son_obj = son()
son_obj.car()
