n = input()
list_n = n.split()

a = int(list_n[1])
b = int(list_n[0])

for i in range(b, a-1, -2):
    print(i, end =" ")