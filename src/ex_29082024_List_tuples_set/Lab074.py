set1 = {"Lets", "Learn", "Python", "Programming", "Python."}
print(len(set1))
for i in set1:
    print(i)

set1.add("Program")
set1.add("Program")
print(set1)
set1.remove("Python.")
print(set1)