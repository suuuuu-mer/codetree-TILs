a = input()
b = input()

len_a = len(a)
len_b = len(b)

list_a = list(a)

while b in a:
    for i in range(len_a - len_b):
        if a[i:i+len_b] == b:
            a = a[:i] + a[i+len_b:]

print(a)