n = input()
list_n = n.split()

sum_val = 0
num = 0

for i in range(10):
    if int(list_n[i]) < 250:
        sum_val += int(list_n[i])
        num += 1
    if int(list_n[i]) >= 250:
        break
    if sum_val == 0:
        sum_val += int(list_n[i])
        num = 10
    

avr = sum_val / num 

print(f"{sum_val} {avr:.1f}")