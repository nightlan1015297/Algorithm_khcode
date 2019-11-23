import sys
while True:
	howmany = int(sys.stdin.readline())
	data = []
	for i in range(howmany):
		dat = sys.stdin.readline().split(" ")
		data.append(dat)
	HWBIG = []
	for dat in data:
		ans = int(dat[0])*int(dat[1])
		HWBIG.append(ans)
	maximus = HWBIG[0]
	for whnum in range(len(HWBIG)):
		if HWBIG[whnum]>maximus:
			maximus = HWBIG[whnum]
	for whnumm in range(len(HWBIG)):
		if HWBIG[whnumm] == maximus:
			break
	print(data[whnumm][0]+" "+data[whnumm][1])