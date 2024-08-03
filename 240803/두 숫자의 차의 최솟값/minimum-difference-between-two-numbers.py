n = int(input())
s = list(map(int,input().split()))

min_val = s[n-1] - s[n-2]

for i in range(n-1, 1, -1):
    if s[i] - s[i-1] <= min_val:
        min_val = s[i] - s[i-1]


print(min_val)