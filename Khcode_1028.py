import sys
a = sys.stdin.readline()
while True:
	data = sys.stdin.readline().split(" ")
	a1,b1,a2,b2 = data
	a1=int(a1)
	b1=int(b1)
	a2=int(a2)
	b2=int(b2)
	if a2<= a1 <=b2 or a2<= b1 <=b2 or (b1>=b2 and a1<=a2):
		print("Yes")
	else:
		print("No")
		