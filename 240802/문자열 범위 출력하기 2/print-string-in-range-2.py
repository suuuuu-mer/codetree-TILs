s = input()
n = int(input())

if n < len(s):
    print(s[:-n-1:-1])
else:
    print(s[::-1])