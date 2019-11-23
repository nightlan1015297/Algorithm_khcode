import sys
while True:
	num = int(sys.stdin.readline())
	for i in range(0,20):
		y = (20 - i)
		x = int(round(pow ( num , 1/y )))
		if (x**y) == num:
			break
	print(x,y) 