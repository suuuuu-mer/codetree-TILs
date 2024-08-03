new_list = []

for _ in range(5):
    arr = list(map(str, input().split()))
    new_list.append(arr)

for i in range(5):
    for j in range(3):
        print(new_list[i][j].upper(), end=" ")
    print()