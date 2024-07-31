n = int(input())
num = list(map(int, input().split()))

new_list = [i ** 2 for i in num]

for j in new_list:
    print(j, end = " ")