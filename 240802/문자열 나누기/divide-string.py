n = int(input())
s = input().split()

string = ""

for i in s:
    string += i

for j in range(0, len(string), 5):
    print(string[j:j+5])