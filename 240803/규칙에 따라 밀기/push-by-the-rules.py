a = input()
l = input()

for i in l:
    if i == "L":
        a = a[1:] + a[0]
    else:
        a = a[-1] + a[:-1]

print(a)