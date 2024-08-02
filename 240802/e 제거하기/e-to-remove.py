s = input()

lists = list(s)

for i in range(len(s)):
    if lists[i] == "e":
        lists.pop(i)
        a = "".join(lists)
        print(a)
        break