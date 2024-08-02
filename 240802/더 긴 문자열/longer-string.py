string = input().split()

str_one = string[0]
str_two = string[1]

if len(str_one) > len(str_two):
    print(f"{str_one} {len(str_one)}")
elif len(str_one) < len(str_two):
    print(f"{str_two} {len(str_two)}")
else:
    print("same")