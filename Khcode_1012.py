import sys
looptime = 0
for number in sys.stdin:
	eachnum = []
	looptime = looptime+1
	count = []
	if looptime > 1: 
		for num in number:
			eachnum.append(num)
		for whnum in range(0,9):
			whnum = str(whnum)
			count.append(eachnum.count(whnum))
		print(number, end=" ")
		for ans in count:
			print(ans, end=" ")
		print(eachnum.count(str(9)))