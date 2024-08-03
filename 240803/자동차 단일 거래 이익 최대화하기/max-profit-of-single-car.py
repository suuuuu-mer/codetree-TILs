n = int(input())
a = list(map(int, input().split()))

min_val = a[0]
i_val = 0

for i in range(n):
    if a[i] < min_val:
        min_val = a[i]
        i_val += i

max_val = 0

for j in range(i_val + 1, n):
    if a[j] > max_val:
        max_val = a[j]

sub = max_val - min_val

if max_val == 0:
    print("0")
else:
    print(sub)