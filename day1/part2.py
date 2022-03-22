f = open("input.TXT", 'r')
List = f.readline() 
cnt = 0

for i in range(0, len(List)):
	if (List[i] == '(') or (List[i] == ')'):
		cnt = cnt + 1

print("Позиция персонажа: " + cnt)
f.close()

newfile = open("output.TXT", "w")
d = str(cnt)
newfile.write(d) 
newfile.close()