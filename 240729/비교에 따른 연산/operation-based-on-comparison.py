int_number = input()
num = int_number.split()
first_number = int(num[0])
second_number = int(num[1])

if first_number > second_number:
    print(first_number * second_number)
else:
    print(second_number // first_number)