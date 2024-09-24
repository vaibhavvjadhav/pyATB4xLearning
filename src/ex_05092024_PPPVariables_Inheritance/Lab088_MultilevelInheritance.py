class GrandFather:
    gold = "2KGS"

    def bhk1(self):
        print("1BHK",self.gold)

class Father(GrandFather):
    diamond = "24Carat"

    def bhk2(self):
        print("2BHK", self.diamond)

class Child(Father):
    silver = "3KGS"
    def bhk3(self):
        print("3BHK", self.silver)

c = Child()
c.gold
c.diamond
c.silver
c.bhk1()
c.bhk2()
c.bhk3()
f = Father()
f.gold
f.diamond
f.bhk1()
f.bhk2()
g = GrandFather()
g.gold
g.bhk1()