sum_val = 0
num = 0

while True:
    n = int(input())

    if 20 <= n < 30:
        sum_val += n
        num += 1
        continue
    else:
        print(f"{sum_val / num:.2f}")
        break