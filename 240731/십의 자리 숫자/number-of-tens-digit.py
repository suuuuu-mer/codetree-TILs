num = list(map(int, input().split()))

count = [0] * 10

for i in range(99):
    if num[i] == 0:
        break
    else:
        count[(num[i] // 10)] += 1

for j in range(1, 10):
    print(f"{j} - {count[j]}")