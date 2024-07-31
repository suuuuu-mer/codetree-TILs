n = input().split()

n1 = int(n[0])
n2 = int(n[1])

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

is_subsequence = False

for i in range(n1 - n2 + 1):
    if list_a[i:i+n2] == list_b:
        is_subsequence = True
        break

if is_subsequence:
    print("Yes")
else:
    print("No")