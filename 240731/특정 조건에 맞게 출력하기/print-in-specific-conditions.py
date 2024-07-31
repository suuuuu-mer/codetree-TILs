num = list(map(int, input().split()))

new = []
i = 0

while True:
    if num[i] == 0:
        break
    elif num[i] % 2 == 1:
        new.append(num[i] + 3)
    else:
        new.append(num[i] // 2)
    
    i += 1

for i in new:
    print(i, end = " ")