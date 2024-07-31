n = int(input())
list_n = list(map(int, input().split()))
new = []

for i in range(n):
    if list_n[i] % 2 == 0:
        new.append(list_n[i])

list_rev = list_n[::-1]

for j in range(len(list_rev)):
    print(j, " ")