n = int(input())

arr = [
    input()
    for i in range(n)
]

s = str(input())

cnt = 0
len_all = 0

for j in arr:
    if j[0] == s:
        cnt += 1
        len_all += len(j)

avr = len_all / cnt

print(f"{cnt} {avr:.2f}")