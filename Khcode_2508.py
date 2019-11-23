import sys
while True:
	Long = int(sys.stdin.readline())
	if Long<0 :
		Long = -Long
		print(Long*2)
	else:
		num = Long-1
		print(num*2+1)
