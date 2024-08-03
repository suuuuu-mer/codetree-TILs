new = []

while True:
    a = input()

    if a == "0":
        break

    else:
        new.append(a)

lists = []

for i in range(len(new)):
    if i % 2 == 0:
        lists.append(new[i])

print(len(new))

for j in lists:
    print(j)