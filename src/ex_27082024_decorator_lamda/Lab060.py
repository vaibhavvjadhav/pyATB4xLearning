def make_pizza(*topping):
    for topin in topping:
        print(topin)

def make_pizza2(*topping, base):
    for topin in topping:
        print(topin)

make_pizza("paneer", "cheese", "olives")
make_pizza2("onion", "paneer", "capsicum", base="thin crust")
