n = int(input())

sum_val = 0
num = 0

for i in range(n):
    a = int(input())

    sum_val += a
    num += 1

avr = sum_val / num

print(f"{sum_val} {avr:.1f}")