n = input()
list_n = n.split()

a = int(list_n[0])
b = int(list_n[1])

multi = 1

for i in range(1, b+1):
    if i % a == 0:
        multi *= i

print(multi)