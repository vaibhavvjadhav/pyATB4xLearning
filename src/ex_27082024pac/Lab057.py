my_shopping_list = ["bread", "milk", "butter"]
print(my_shopping_list[0])
print(len(my_shopping_list))

def bring_more(my_list):
    more_item = input("Enter the item")
    my_list.append(more_item)

    #print(my_list)
    return my_list

new_list = bring_more(my_shopping_list)
print(new_list)