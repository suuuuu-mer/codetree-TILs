sum_val = 0

while True:
    n = int(input())
    if n % 2 == 0:
        sum_val += 1
        print(n // 2)
        if sum_val == 3:
            break