s = input()
list_s = s.split()

a = int(list_s[0])
b = int(list_s[1])

if a > b:
    for i in range (a, b-1, -1):
        print(i, end = " ")
else:
    for i in range (b, a-1, -1):
        print(i, end = " ")