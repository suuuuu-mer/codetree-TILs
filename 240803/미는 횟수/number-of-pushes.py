a = input()
b = input()

leng = len(a)

count = 0

for _ in range(leng):
    if a == b:
        count += 1
        break
    else:
        a = a[-1] + a[:-1]

if count == 0:
    print(-1)
else:
    print(count)