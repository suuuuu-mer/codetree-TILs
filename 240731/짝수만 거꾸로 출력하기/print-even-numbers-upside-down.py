n = int(input())
list_n = list(map(int, input().split()))
new = []

for i in range(n):
    if list_n[i] % 2 == 0:
        new.append(list_n[i])

list_rev = new[::-1]

for j in list_rev:
    print(j, end = " ")