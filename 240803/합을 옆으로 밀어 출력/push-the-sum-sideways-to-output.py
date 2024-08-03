n = int(input())

nums = [
	input()
	for _ in range(n)
]

sum_val = 0

for i in nums:
    sum_val += int(i)

str_sum = str(sum_val)
total = str_sum[1:] + str_sum[0]

print(total)