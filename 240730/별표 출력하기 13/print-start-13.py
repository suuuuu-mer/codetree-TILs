n = int(input())

for i in range(n): #(0,1,2)
    if i % 2 == 0:
        for _ in range(n-(i//2)):
            print('*', end=' ')
    else:
        for _ in range(n-i-1):
            print('*', end=' ')
    print()

for i in range(n,0,-1): #(5,4,3,2,1)
    if i%2==1:
        for _ in range(n-(i-1)//2):
            print('*', end=' ')
    else:
        for _ in range(n-1-(i//2)):
            print('*', end=' ')
    print()