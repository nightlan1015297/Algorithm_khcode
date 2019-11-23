import sys
a = sys.stdin.readline()
while True :
	num =int(sys.stdin.readline())
	x = int(round(pow(num,1/2)))
	if x**2 == num:
		print("Yes")
	else:
		print("No")
