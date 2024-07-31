n = int(input())
num = list(map(int, input().split()))

max_val = 0
min_val = num[0]

for i in num[1:]:
    if i < min_val:
        min_val = i
        
for j in num[num.index(min_val):]:
    if j > max_val:
        max_val = j
    else:
        break


if max_val == 0 :
    print(0)
else:
    print(max_val - min_val)