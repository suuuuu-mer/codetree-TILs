a = input()

length = len(a)

fir_char = a[0]
sec_char = a[0]

num_char = 1
encoded = ""

for i in range(1,length) :
    sec_char = a[i]
    if sec_char == fir_char :
        num_char += 1
    else :
        encoded += fir_char
        encoded += str(num_char)
        
        num_char = 1
        fir_char = sec_char

encoded += fir_char
encoded += str(num_char)
                   
print(len(encoded))
print(encoded)