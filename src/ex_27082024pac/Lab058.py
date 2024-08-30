mylist_Learning = ["Learn","Python"]
print(mylist_Learning[0])
print(len(mylist_Learning))

def learning(newList):
    moreList = input("Enter the Learning")
    newList.append(moreList)
    newList.insert(4, moreList)
    return newList

l = learning(mylist_Learning)
print(l)
