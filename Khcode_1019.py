import sys
while True:
	allnum = []
	dataclass = sys.stdin.readline()
	dataclass = dataclass.split(" ")
	dataclass = list(map(int,dataclass))
	for i in range(dataclass[0]):
		data = sys.stdin.readline()
		data = data.split(" ")
		data = list(map(int,data))
		allnum = allnum + data
	for i in range(dataclass[1]):
		anstr = ""
		for x in range(i,len(allnum),dataclass[1]):
			anstr =anstr+str(allnum[x])+" "
		print(anstr) 
