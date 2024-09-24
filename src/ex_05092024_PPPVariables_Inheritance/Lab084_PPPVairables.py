class MyClass:
    public_var = "I am the Public Variable"
    _protected_var = "I am the Protected Variable"
    __private_var = "I am the Private Varaible"
    print(__private_var)
obj = MyClass
public = obj.public_var
print(public)
protected = obj._protected_var
print(protected)
#private = obj.__private_var # private variable cannot be used outside the class
#print(private)
