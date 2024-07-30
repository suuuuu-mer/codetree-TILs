n = input()
list_n = n.split()

start = int(list_n[0])
end = int(list_n[1])

sum_val = 0

for i in range(start, end + 1):
    cnt = 0
    for j in range(1, i):
        if (i % j) == 0:
            cnt += j
    if cnt == i:
        sum_val += 1
    
print(sum_val)