import sys
looptime = 0
for num in sys.stdin:
	looptime = looptime + 1
	if looptime%2 == 0:
		numlist = []
		Acount = []
		for t in num:
			numlist.append(t)
		ans = []
		for whnum in range(0,10):
			Acount.append(int(numlist.count(str(whnum))))
		maximus = max(Acount)
		for a in range(0,10):
			if Acount[a] == maximus:
				ans.append(a)
		for i in range(0,len(ans)-1):
			print(ans[i] , end =" ")
		print(ans[len(ans)-1])



