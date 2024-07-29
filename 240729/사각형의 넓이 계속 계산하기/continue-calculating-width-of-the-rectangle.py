while True:
    n = input()
    list_n = n.split()

    a = int(list_n[0])
    b = int(list_n[1])
    c = str(list_n[2])
    
    if c != "C":
        print(a * b)
        continue
    else:
        print(a * b)
        break