s = input()
l = len(s)

print(s)

for i in range(l):
    print(s[-1] + s[:-1])
    s = s[-1] + s[:-1]