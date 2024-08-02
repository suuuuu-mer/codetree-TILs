arr = [
    input()
    for i in range(10)
]

s = input()
new = []

for i in arr:
    if i[-1] == s:
        new += i
        print(i)
    
if len(new) == 0:
    print("None")