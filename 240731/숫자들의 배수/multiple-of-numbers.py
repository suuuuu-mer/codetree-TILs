n = int(input())

i = 1
count = 0

while True:
    print(n * i, end = " ")
    
    if (n * i) % 5 == 0:
        count += 1
    if count == 2:
        break

    i += 1