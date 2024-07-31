n = list(map(int, input().split()))

a = n[0]
b = n[1]

new = [a, b]

for i in range(3, 11):
    new.append((new[-1] + new[-2]) % 10)

for j in new:
    print(j, end = " ")