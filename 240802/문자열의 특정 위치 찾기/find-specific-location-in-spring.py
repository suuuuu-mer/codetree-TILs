s = input().split()

a = s[0]
b = s[1]

if b in a:
    print(a.find(b))
else:
    print("No")