s = input()
list_s = s.split()

a = int(list_s[0])
b = int(list_s[1])

if a > 0:
    for i in range(b):
        print(a, end = "")
else:
    print(0)