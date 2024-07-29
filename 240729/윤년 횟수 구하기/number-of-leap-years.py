y = int(input())

luna = 0

for i in range(1, y + 1):
    if ((i % 4 == 0) and (i % 100) != 0) or (i % 400) == 0:
        luna += 1

print(luna)