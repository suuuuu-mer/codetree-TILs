a = input()
b = a.split()

first_num = int(b[0])
second_num = int(b[1])

if first_num > second_num:
    print(first_num)
else:
    print(second_num)