s = input()

count_one = 0
count_two = 0

length = len(s)


for i in range(length-1):
    if s[i:i+2] == 'ee':
        count_one += 1


for j in range(length-1):
    if s[j:j+2] == 'eb':
        count_two += 1

print(count_one, count_two)