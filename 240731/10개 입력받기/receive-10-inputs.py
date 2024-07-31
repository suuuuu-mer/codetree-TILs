n = list(map(int, input().split()))
new = []
num = 0

for i in range(len(n)):
    if n[i] == 0:
        break
        
    new.append(n[i])
    num += 1


sum_list = sum(new)
avr = sum_list / num 

print(f"{sum_list} {avr:.1f}")