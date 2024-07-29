n = input()
list_n = n.split()

first = int(list_n[1])
second = int(list_n[0])

i = second

while i >= first:
    print(i, end = " ")
    i -= 2