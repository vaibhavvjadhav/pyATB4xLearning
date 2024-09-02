# List is collection of item
# List can contain duplicates, multiple data types

my_list = [1,2,3]
my_list1 = [1, 3.14, True, "Python"]

print(my_list)
print(len(my_list))
my_list[0] = "Vaibhav"
print(my_list[0])
#print(my_list[4])

print(my_list1)
print(len(my_list1))
for element in my_list1:
    print(element)

#append - single object at the end of the list
my_list1.append("Programming")
my_list1.append(2) #Append the object at the end of list

# Extend - Extends another list to existing list
my_list1.extend([3,4,5,6,7])
my_list1.extend(["Learning", "4X"])
print(my_list1)

print("-------------------------------------")

#insert object at index
my_list1.insert(1,"The") # insert the element at specified index
print(my_list1)

my_list1.insert(0,0)
print(my_list1)

my_list1.insert(-1,"Program")
print(my_list1)

#remove
my_list1.remove("Program")
print(my_list1)

#copying the list
my_copy_list = my_list1.copy()
print(my_copy_list)

print("-------------------------------------")
print("-------------------------------------")

my_copy_list = my_list1.copy()
my_list1.clear()
print(my_list1)
print(my_copy_list)

print("-------------------------------------")

random_list = [0, 1, 2, 3, 4, 5, 10, 9, 8, 7, 6]
random_list.sort()
print(random_list)

print("-------------------------------------")

random_list.reverse()
print(random_list)

new_list = ["Vaibhav", "Jadhav"]
new_list.reverse()
print(new_list)


