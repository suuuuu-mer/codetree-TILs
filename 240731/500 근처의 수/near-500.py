num = list(map(int, input().split()))

up = []
down = []

for i in num:
    if i > 500:
        up.append(i)
    if i < 500:
        down.append(i)

print(max(down), min(up))