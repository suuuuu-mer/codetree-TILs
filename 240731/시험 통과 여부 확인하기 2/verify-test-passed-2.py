n = int(input())
nums = [ list(map(int, input().split())) for i in range(n) ]
number = 0

for j in range(n):
    if sum(nums[j]) / 4 >= 60:
        print("pass")
        number += 1
    else:
        print("fail")

print(number)