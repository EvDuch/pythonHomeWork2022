f = open("input.txt", 'r')
List = f.readline() 
op = 0
cl = 0

for i in range(0, len(List)):
	if List[i] == '(':
		op += 1
	if List[i] == ')':
		cl += 1
res = op - cl
print("Количество раз когда Санта поднимется на этаж: " + str(op))
print("Количество раз когда Санта опустится на этаж: " + str(cl))
print("Санта окажется на " + str(res) + " этаже.")
f.close()

newfile = open("output1.txt", "w")
d = str(res)
newfile.write(d) 
newfile.close()

