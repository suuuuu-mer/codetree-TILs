n = input()
list_n = n.split()

sum_val = 0

for i in range(8):
    sum_val += float(list_n[i])

avr = sum_val / 8

print(f"{avr:.1f}")