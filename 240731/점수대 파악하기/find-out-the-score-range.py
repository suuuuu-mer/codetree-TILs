num = list(map(int, input().split()))

count = [0] * 11

for i in range(len(num)):
    if num[i] == 0:
        break
    else:
        count[num[i] // 10] += 1

count_rev = count[::-1]

for j in range(10):
    print(f"{100 - (j * 10)} - {count_rev[j]}")