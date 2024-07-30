n = input()
list_n = n.split()

a = int(list_n[0])
b = int(list_n[1])


for i in range(1, 10):

    for j in range(b, a-1, -2):
        print(f"{j} * {i} = {j * i}", end = "")
        if j > a:
            print(" /", end = " ")
    print()