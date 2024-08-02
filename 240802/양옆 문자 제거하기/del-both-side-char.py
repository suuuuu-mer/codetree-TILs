s = input()
length = len(s)

arr= list(s)
arr.pop(length-2)
arr.pop(2)

s = "".join(arr)

print(s)