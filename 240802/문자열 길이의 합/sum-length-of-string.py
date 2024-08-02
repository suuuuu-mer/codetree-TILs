n = int(input())

new = []
num = 0

for i in range(n):
    string = input()
    new += string

    if string[0] == "a":
        num += 1

new_num = len(new)

print(new_num, num)