new_list = [1, 2, 3, 4, 5]
print(new_list.pop())
print(new_list)

new_list[3] ='25' # List are Mutable in Nature - value can change
print(new_list)

my_tuple = (1, 2, 3, 4, 5)
#my_tuple[3] = '45' tuples are Imutable in Nature - value cannot change
print(my_tuple)
print("-------------------------------------")

#converting tuple into list
my_list = list(my_tuple)
print(my_list)

#converting list into tuple
my_tuple = tuple(my_list)
print(my_tuple)