s = input()

a = s[1]
b = s[0]

encoded = ""

for i in range(len(s)):
    if s[i] == a:
        encoded += b
    else:
        encoded += s[i]
    
print(encoded)