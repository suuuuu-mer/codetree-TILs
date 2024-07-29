a = input()
list_a = a.split()

c = list_a[0]
n = int(list_a[1])

if c == "A":
    for i in range (1, n+1, 1):
        print(i, end = " ")
else:
    for i in range (n, 0, -1):
        print(i, end = " ")