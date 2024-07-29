n = int(input())

satisfied = True

for i in range (1, n + 1):
    if i * n == n:
        satisfied = False

if satisfied == False:
    print("P")
else:
    print("C")