n = int(input())
if_not = False


for i in range(2, n):
    if n % i == 0:
        if_not = True

if if_not == True:
    print("C")
else:
    print("N")