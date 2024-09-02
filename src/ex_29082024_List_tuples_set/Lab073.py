set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = set1.union(set2)
print(set3)

set3 = set1.intersection(set2)
print(set3)

set3 = set1.difference(set2)
print(set3)

set3 = set2.difference(set1)
print(set3)

#issubset - every element should be present in set

set01 = {1, 2, 3, 4, 5}
set02 = {3, 4, 8}
sub03 = set01.issubset(set02)
print(sub03)

