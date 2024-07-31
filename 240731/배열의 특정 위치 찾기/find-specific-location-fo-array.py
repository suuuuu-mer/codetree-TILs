n = list(map(int, input().split()))

filtered_n = n[::2]

sum_n = 0

for i in filtered_n:
    sum_n += n[i]

sum_j = 0

for j in range(2, 10, 3):
    sum_j += n[j]

avr = sum_j / 3

print(f"{sum_n} {avr:.1f}")