new = []

while True:
    string = input()
    if string == "END":
        break
    else:
        new.append(string)
        
for i in range(len(new)):
    print(new[i][::-1])