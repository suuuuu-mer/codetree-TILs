a = input()
b = input()

new_a = ""
new_b = ""

for i in a:
    if i >= '0' and i <= '9':
        new_a += i

for j in b:
    if j >= '0' and j <= '9':
        new_b += j


print(int(new_a) + int(new_b))