n = int(input())

new = []

new.append(1)
new.append(n)


while new[-1] < 100:
    new.append(new[-1] + new[-2])

for i in new:
    print(i, end = " ")