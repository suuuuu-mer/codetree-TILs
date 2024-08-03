b = input().split()
n = int(b[0])
a = b[1]

string = [
    input()
    for i in range(n)
]

count = 0

for j in range(n):
    if string[j] == a:
        count += 1


print(count)