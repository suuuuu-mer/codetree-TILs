a = input()
b = a.split()

height = int(b[0])
weight = int(b[1])

bmi = (10000 * weight) // (height * height)

print(bmi)
if bmi >= 25:
    print("Obesity")