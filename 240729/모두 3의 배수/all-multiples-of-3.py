satisfied = False

for i in range(5):
    n = int(input())
    
    if n % 3 == 0:
        continue
    else:
        satisfied = True

if satisfied == True:
    print(0)
else:
    print(1)