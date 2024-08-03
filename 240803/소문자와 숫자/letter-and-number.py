string = input()

for elem in string:
	if(elem >= 'A' and elem <= 'Z') or (elem >= 'a' and elem <= 'z') or elem.isdigit():
		print(elem.lower(), end="")