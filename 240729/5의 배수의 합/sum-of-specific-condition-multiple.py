n = input()
list_n = n.split()

a = int(list_n[0])
b = int(list_n[1])

sum_val = 0

if a < b:
    for i in range(a, b+1):
        if i % 5 == 0:
            sum_val += i
else:
    for i in range(b, a+1):
        if i % 5 == 0:
            sum_val += i

print(sum_val)