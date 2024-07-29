n = input()
list_n = n.split()

first = int(list_n[0])
second = int(list_n[1])

while first <= second:
    print(first, end = " ")
    first += 2