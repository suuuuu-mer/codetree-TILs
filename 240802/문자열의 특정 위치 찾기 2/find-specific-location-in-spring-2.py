lists = ["apple", "banana", "grape", "blueberry", "orange"]

string = input()

new_list = []

for i in lists:
    if string in i[2] or string in i[3]:
        new_list.append(i) 

for j in new_list:
    print(j, end ="\n")
        
print(len(new_list))