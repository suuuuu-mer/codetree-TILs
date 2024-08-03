a, b = input().split()

new_a = ""
new_b = ""

for i in a:
    if not i.isdecimal():
        break
    
    new_a += i

for j in b:
    if not j.isdecimal():
        break
    
    new_b += j

new_a = int(new_a)
new_b = int(new_b)

print(new_a + new_b)