num = input().split()

n = int(num[0])
m = int(num[1])

a = list(map(int, input().split()))

cnt = 0

for i in a:
    if i == m:
        cnt += 1

print(cnt)