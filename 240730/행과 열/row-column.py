n = input()
list_n = n.split()

a = int(list_n[0])
b = int(list_n[1])

for i in range(1, a+1):
    for j in range(1, b+1):
        print(i * j, end = " ")
    print()