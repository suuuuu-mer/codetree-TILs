a = input()
b = input()

c = a.split()
d = b.split()

age_a = int(c[0])
age_b = int(d[0])
sex_a = c[1]
sex_b = d[1]

if (sex_a == "M" and age_a >= 19) or (sex_b == "M" and age_b >= 19):
    print(1)
else:
    print(0)