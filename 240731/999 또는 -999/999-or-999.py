n = list(map(int, input().split()))

max_val = n[0]
min_val = n[0]


for i in n:
    if i == 999 or i == -999:
        n.pop()
        break

for j in n:
    if j >= max_val:
        max_val = j
    if j <= min_val:
        min_val = j

print(max_val, min_val)