n = int(input())
numbers = list(map(int, input().split()))

min_val = numbers[0]


for i in numbers[1:]:
    if i <= min_val:
        min_val = i

num = 0

for j in numbers:
    if j == min_val:
        num += 1

print(min_val, num)