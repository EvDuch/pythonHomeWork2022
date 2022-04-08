f = open("input.txt", 'r')
List = f.readline() 
op = 0
cl = 0
cnt = 0
for i in range(0, len(List)):
	cnt+=1
	if List[i] == '(':
		op += 1
	if List[i] == ')':
		cl += 1
	if op - cl == -1:
		break
print("Ответ: " + str(cnt))
f.close()

newfile = open("output2.txt", "w")
d = str(cnt)
newfile.write(d) 
newfile.close()

