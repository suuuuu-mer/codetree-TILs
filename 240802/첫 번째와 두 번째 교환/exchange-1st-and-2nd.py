s = input()

fir = s[0]
sec = s[1]

encoded = ""

for i in range(len(s)):
    if s[i] == fir:
        encoded += sec
    elif s[i] == sec:
        encoded += fir
    else:
        encoded += s[i]

print(encoded)