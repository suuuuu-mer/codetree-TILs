n = input()
new = []

for i in range(len(n)):
    if i % 2 == 1:
        new += n[i]

for j in new[::-1]:
    print(j, end = "")