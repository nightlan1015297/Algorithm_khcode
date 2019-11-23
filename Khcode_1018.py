import sys
while True:
	datas = []
	lines = sys.stdin.readline()
	for strings in range(int(lines)):
		datas.append(sys.stdin.readline())
	for strindex in range(len(datas)-1):
		print(datas[len(datas)-strindex-1],end ="")
	print(datas[0])
