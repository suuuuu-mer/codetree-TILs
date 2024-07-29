a = input()
b = a.split()

first_num = int(b[0])
second_num = int(b[1])
third_num = int(b[2])

if first_num <= second_num and first_num <= third_num:
    print(first_num)
elif second_num <= first_num and second_num <= third_num:
    print(second_num)
else:
    print(third_num)