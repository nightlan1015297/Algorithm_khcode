import sys
a = int(sys.stdin.readline())
for i in range(a):
	num = int(sys.stdin.readline())
	bnum = bin(num)
	print(bnum[2::])