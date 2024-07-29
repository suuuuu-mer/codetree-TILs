n = input()
list_n = n.split()

a = int(list_n[0])
b = int(list_n[1])

for i in range (b, a-1, -1):
    print(i, end = " ")