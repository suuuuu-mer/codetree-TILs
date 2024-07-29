sum_val = 0
num = 0

for i in range(10):
    a = int(input())

    if 0 <= a <= 200:
        sum_val += a
        num += 1

aver_val = sum_val / num

print(f"{sum_val} {aver_val:.1f}")