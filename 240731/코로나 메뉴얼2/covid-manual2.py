count = [0] * 4

for i in range(3):
    num = input().split()
    
    a = num[0]
    b = int(num[1])

    if a == "Y" and b >= 37:
        count[0] += 1
    elif a == "N" and b >= 37:
        count[1] += 1
    elif a == "Y" and b < 37:
        count[2] += 1
    else:
        count[3] += 1

if count[0] >= 2:
            count.append("E")
    
for j in count:
    print(j, end = " ")