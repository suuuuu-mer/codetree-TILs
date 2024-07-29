n = input()
list_n = n.split()

a = int(list_n[0])
b = int(list_n[1])

if_not = False

num = 0

for i in range (a, b+1):
    if 1920 % i == 0 and 2880 % i == 0:
        if_not = True
    
if if_not == True:
    print(1)
else:
    print(0)