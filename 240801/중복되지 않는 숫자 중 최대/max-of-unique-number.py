n = int(input())
nums = list(map(int, input().split()))

max_list = []
ori_list = []

for i in nums:
    if i not in max_list:
        max_list.append(i)
    else:
        if i not in ori_list:
            ori_list.append(i)
            max_list.remove(i)

if max_list is None:
    print(-1)
else:
    print(max(max_list))