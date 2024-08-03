s = input()

sum_val = 0

for i in s:
    if i >= '0' and i <= '9':
        sum_val += int(i)

print(sum_val)