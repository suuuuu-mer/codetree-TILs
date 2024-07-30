n = int(input())
sub = input()
list_sub = sub.split()

sum_val = 0

for i in range(n):
    sum_val += float(list_sub[i])

avr = sum_val / n

print(f"{avr:.1f}")

if avr >= 4.0:
    print("Perfect")
elif avr >= 3.0:
    print("Good")
else:
    print("Poor")