n, q = map(int, input().split())
list_one = list(map(int, input().split()))

for i in range(q):
    lists = list(map(int, input().split()))

    if lists[0] == 1:
        print(list_one[lists[1]-1])

    elif lists[0] == 2:
        if lists[1] in list_one:
            print(list_one.index(lists[1]) + 1)
        else:
            print("0")

    elif lists[0] == 3:
        for j in range(lists[1]-1, lists[2]):
            print(list_one[j], end = " ")
        print()