n = int(input())
num = list(map(int, input().split()))

new = []

for i in range(n):
    if num[i] % 2 == 0:
        new.append(num[i])
    else:
        continue

for j in new:
    print(j, end = " ")