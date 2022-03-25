array = []
with open('input.txt', 'r') as INPUT:
	line = INPUT.readlines()
	line = str(line)[2:-2]
	array.append([0,0])
	y=0
	x=0
	l = 0
	for i in line:
		l += 1
		if l % 2 == 0:
			continue
		elif i == '>':
			x += 1
		elif i == '<':
			x += -1
		elif i == '^':
			y += 1
		elif i == 'v':
			y += -1
		array.append([x,y])
	a=0
	b=0
	l=0
	for i in line:
		l += 1 
		if l % 2 != 0:
			continue
		elif i == '>':
			a += 1
		elif i == '<':
			a += -1
		elif i == '^':
			b += 1
		elif i == 'v':
			b += -1
		array.append([a,b])	
	array1 = array.copy()
	for j in array1:
		if array.count(j) > 1:
			for k in range(array.count(j) - 1):
				array.remove(j)
	print('Домов,  получивших хотябы один подарок ', str(len(array)))
INPUT.close()
with open('output2.txt','w') as output:
	output.write(str(len(array)))