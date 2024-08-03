arr_2d = [
	list(map(int, input().split()))
	for _ in range(2)
]

for i in range(2):
    hor_sum = 0
    for j in range(4):
        hor_sum += arr_2d[i][j]
    print(f"{hor_sum/4:.1f}", end = " ")
print()

for i in range(4):
    vet_sum = 0
    for j in range(2):
        vet_sum += arr_2d[j][i]
    print(f"{vet_sum/2:.1f}", end = " ")
print()

total = 0

for i in range(2):
    for j in range(4):
        total += arr_2d[i][j]
print(f"{total/8:.1f}")