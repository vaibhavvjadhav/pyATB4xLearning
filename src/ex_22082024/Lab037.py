# program to print even number from 0 to 100
for i in range(0, 100):
    if i % 2 == 0:  # if reminder is 0 print the number which are even
        print(i, end='|')
    else:
        pass
j = 0
while j <= 100:
    if j % 2 != 0:
        print(j, end='@')
    j = j + 1
