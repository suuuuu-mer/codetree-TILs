str_one = len(input())
str_two = len(input())
str_three = len(input())

lists = [str_one, str_two, str_three]

max_val = 0
min_val = 21

for i in lists:
    if i > max_val:
        max_val = i

for j in lists:
    if j < min_val:
        min_val = j

print(max_val - min_val)