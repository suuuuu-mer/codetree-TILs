s_1 = input()
s_2 = input()

count_1 = 0


for i in range(len(s_1)-len(s_2)+1):
    if s_1[i:i+len(s_2)] == s_2:
        count_1 += 1

if count_1 >= 1:
    print(s_1.index(s_2))
else:
    print("-1")