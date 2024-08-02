s = input()
length = len(s)

arr= list(s)
arr.pop(length-2)
arr.pop(1)

s = "".join(arr)

print(s)