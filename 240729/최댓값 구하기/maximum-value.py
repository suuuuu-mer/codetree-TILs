num = input()
list_num = num.split()

a = int(list_num[0])
b = int(list_num[1])
c = int(list_num[2])

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
elif c >= a and c >= b:
    print(c)