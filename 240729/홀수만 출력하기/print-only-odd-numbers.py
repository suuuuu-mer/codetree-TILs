n = input()

list_n = n.split()

for i in list_n:
    if i % 2 == 1 and i % 3 == 0:
        print(i)