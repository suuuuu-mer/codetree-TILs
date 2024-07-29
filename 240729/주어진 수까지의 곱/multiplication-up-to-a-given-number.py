n = input()
list_n = n.split()

a = int(list_n[0])
b = int(list_n[1])

multiple = 1

for i in range(a, b+1):
    multiple *= i

print(multiple)