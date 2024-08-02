a = input()
b = input()

count = 0

for i in range(len(a)-1):
    if a[i:i+2] == b:
        count += 1

print(count)