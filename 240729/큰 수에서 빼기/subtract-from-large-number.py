a = input()
b = a.split()

first_number = int(b[0])
second_number = int(b[1])

if first_number > second_number:
    print(first_number - second_number)
else:
    print(second_number - first_number)