a = input()
b = a.split()

first_num = int(b[0])
second_num = int(b[1])

if first_num < second_num:
    print(1, end = " ")
else:
    print(0, end = " ")

if first_num == second_num:
    print(1)
else:
    print(0)