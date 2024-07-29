n = int(input())
num = 0

while True:
    if n == 1:
        break
    if n % 2 == 0:
        n = n // 2
        num += 1
    else:
        n = n * 3 + 1
        num += 1

print(num)