n = int(input())

num = list(map(int, input().split()))

count = [0] * 10
for i in num:
    count[i] += 1

for j in range(1, 10):
    cnt = count[j]
    print(cnt)