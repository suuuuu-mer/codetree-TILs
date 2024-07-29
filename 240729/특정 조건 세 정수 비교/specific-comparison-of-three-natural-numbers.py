a = input()
b = a.split()

first_num = int(b[0])
second_num = int(b[1])
third_num = int(b[2])

if first_num <= second_num and first_num <= third_num:
    print(1, end = " ")
else:
    print(0, end = " ")

if first_num == second_num == third_num:
    print(1, end = " ")
else:
    print(0, end = " ")