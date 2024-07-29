n = input()
list_n = n.split()

a = int(list_n[0])
b = int(list_n[1])
c = int(list_n[2])

if_not = False

for i in range (a, b+1):
    if i % c == 0:
        if_not = True

if if_not == True:
    print("YES")
else:
    print("NO")