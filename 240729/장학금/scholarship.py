a = input()
b = a.split()

mid = int(b[0])
final = int(b[1])

if mid >= 90:
    if final>= 95:
        print(100000)
    elif final >= 90:
        print(50000)
    else:
        print(0)
else:
    print(0)