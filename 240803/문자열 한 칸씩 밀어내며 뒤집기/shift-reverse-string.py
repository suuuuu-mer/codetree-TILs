s = input().split()

a = s[0]
b = int(s[1])

num = [
    input()
    for i in range(b)
]

for i in range(b):
    if num[i] == "1":
        a = a[1:] + a[0]
        print(a)
    elif num[i] == "2":
        a = a[-1] + a[:-1]
        print(a)
    else:
        a = a[::-1]
        print(a)