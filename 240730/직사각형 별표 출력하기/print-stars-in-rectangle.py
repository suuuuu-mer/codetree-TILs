a = input()
list_a = a.split()

n = int(list_a[0])
m = int(list_a[1])

for i in range(n):
    for i in range(m):
        print("* ", end="")
    print()