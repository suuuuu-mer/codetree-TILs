n = list(map(int, input().split()))

sum_val = 0

for i in range(len(n)):
    if n[i] == 0:
        sum_val = n[i - 1] + n[i - 2] + n[i - 3]
        break
    else:
        sum_val += n[i]

print(sum_val)