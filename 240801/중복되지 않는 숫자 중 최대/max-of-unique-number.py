n = int(input())
nums = list(map(int, input().split()))

max_val = 0

for i in nums:
    if i > max_val:
        max_val = i
    elif i == max_val:
        max_val = -1

print(max_val)