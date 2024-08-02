a = input()
b = input()

a_space = a.split()
b_space = b.split()

space = a_space + b_space

for i in space:
    print(i, end="")