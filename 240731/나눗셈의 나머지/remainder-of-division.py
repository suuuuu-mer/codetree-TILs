n = input().split()

a = int(n[0])
b = int(n[1])

count = [0] * 10


while a > 1:
    count[(a % b)] += 1
    a //= b

sum_val = 0

for j in range(10):
    if count[j] >= 1:
        sum_val += (count[j] ** 2)

print(sum_val)