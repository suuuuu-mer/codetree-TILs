n = list(map(int, input().split()))

sum_odd = 0
sum_even =0


for i in range(1, 10, 2):
    sum_odd += n[i]

for j in range(0, 10, 2):
    sum_even += n[j]

if sum_even > sum_odd:
    print(sum_even - sum_odd)
else:
    print(sum_odd - sum_even)