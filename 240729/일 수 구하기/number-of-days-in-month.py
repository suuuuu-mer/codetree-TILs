m = int(input())

if m % 2 == 1:
    if m <= 7:
        print(31)
    else:
        print(30)
else:
    if m == 2:
        print(28)
    elif m <= 6:
        print(30)
    else:
        print(31)