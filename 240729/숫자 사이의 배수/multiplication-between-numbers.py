n = input()
list_n = n.split()

a = int(list_n[0])
b = int(list_n[1])

sum_val = 0
num = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum_val += i
        num += 1

print(f"{sum_val} {sum_val / num:.1f}")