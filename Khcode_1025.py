import sys

while True:

	size = int(sys.stdin.readline())
	data = []
	for readdata in range(2*size):
		data.append(sys.stdin.readline().strip("\n").split(" "))
	
	quatbturn = []
	
	for whichnum in range(size):
		num = []
		for i in range(size):
			num.append(data[size+i][whichnum])
		quatbturn.append(num)
	
	quata =[]
	
	for i in range(size):
		quata.append(data[i])
	ans =[]
	for quatawhline in range(size):
		for quatbwhline in range(size):
			anse = 0
			for whnuminquat in range(size):
				answer = int(quata[quatawhline][whnuminquat])*int(quatbturn[quatbwhline][whnuminquat])
				anse = anse + answer
			ans.append(anse)
	for lane in range(size):
		for whnum in range(size-1):
			print(ans[(lane*size+whnum)],end=' ')
		print(ans[(lane*size+size-1)])



