n = list(map(int, input().split()))

sum_n = 0

for i in range(1, 10, 2):
    sum_n += n[i]

sum_j = 0

for j in range(2, 10, 3):
    sum_j += n[j]

avr = sum_j / 3

print(f"{sum_n} {avr:.1f}")