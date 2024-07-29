a = input()
b = input()

c = a.split()
d = b.split()

math_a = int(c[0])
math_b = int(d[0])

eng_a = int(c[1])
eng_b = int(d[1])

if math_a > math_b:
    print("A")
elif math_b > math_a:
    print("B")
elif math_a == math_b:
    if eng_a > eng_b:
        print("A")
    elif eng_b > eng_a:
        print("B")