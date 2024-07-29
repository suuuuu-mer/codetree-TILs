a = input()
b = input()
c = input()

list_a = a.split()
list_b = b.split()
list_c = c.split()

cat_a = list_a[0]
cat_b = list_b[0]
cat_c = list_c[0]

tem_a = int(list_a[1])
tem_b = int(list_b[1])
tem_c = int(list_c[1])

if cat_a == "Y" and tem_a >= 37:
    if cat_b == "Y" and tem_b >= 37:
        print("E")
    else:
        if cat_c == "Y" and tem_c >= 37:
            print("E")
        else:
            print("N")
else:
    print("N")