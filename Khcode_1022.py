import sys
while True:
	strinG = sys.stdin.readline().strip()
	Hasbeencount = False
	lastword = strinG[0]
	counter = 0
	for word in strinG[1::]:
		if word == lastword:
			if Hasbeencount == False:
				counter =counter+2
				Hasbeencount = True
			elif Hasbeencount == True:
				counter =counter+1
				Hasbeencount = True
		else:
			Hasbeencount = False
		lastword = word
	print(counter)