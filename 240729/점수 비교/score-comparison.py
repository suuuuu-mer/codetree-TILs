a = input()
b = input()

list_a = a.split()
list_b = b.split()

math_a = int(list_a[0])
math_b = int(list_b[0])

eng_a = int(list_a[1])
eng_b = int(list_b[1])

if math_a > math_b and eng_a > eng_b:
    print(1)
else:
    print(0)