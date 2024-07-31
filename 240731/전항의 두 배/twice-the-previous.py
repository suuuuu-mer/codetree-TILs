num = list(map(int, input().split()))
new = []

new.append(num[0])
new.append(num[1])

for i in range(3, 11):
    new.append( new[-1] + (2 * new[-2]) )

for j in new:
    print(j, end = " ")