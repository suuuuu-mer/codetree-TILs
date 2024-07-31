n = list(map(int, input().split()))
new = []

num = 0

for i in range(len(n)):
    if n[i] == 0:
        break

    if n[i] % 2 == 0:
        new.append(n[i])
        num += 1

sum_val = sum(new)

print(f"{num} {sum_val}")