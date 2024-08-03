a, b = input().split()

sum_val = ord(a) + ord(b)

if ord(a) > ord(b):
    div_val = ord(a) - ord(b)
else:
    div_val = ord(b) - ord(a)

print(sum_val, div_val)