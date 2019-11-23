import sys
while True:
	times = sys.stdin.readline()
	for i in range(int(times)):
		Str = sys.stdin.readline().strip()
		new = Str[::-1]
		if Str==new :
			print("Yes")
		else:
			print("No")
	