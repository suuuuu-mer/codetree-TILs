c = input()
list_c = c.split()

a = int(list_c[0])
n = int(list_c[1])
i = 1

while i <= n:
    print(a + (n * i))
    i += 1