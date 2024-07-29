a = input()
b = a.split()

first = int(b[0])
second = int(b[1])
third = int(b[2])

if first >= second:
    if first >= third:
        if second >= third:
            print(second)
        else:
            print(third)
    else:
        print(first)
elif second >= first:
    if second >= third:
        if first >= third:
            print(first)
        else:
            print(third)
    else:
        print(second)