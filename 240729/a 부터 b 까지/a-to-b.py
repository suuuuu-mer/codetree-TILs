s = input()
list_s = s.split()

a = int(list_s[0])
b = int(list_s[1])
i = a

while i <= b:
    print(i, end = " ")
    if i % 2 == 1:
        i *= 2
    else:
        i += 3