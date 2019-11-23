import sys
for numbers in sys.stdin:
	numlist = numbers.split()
	if len(numlist)>1:
		new = numlist[::-1]
		for i in range(0,len(numlist)-1):
			print(new[i],end =" ")
		print(new[len(new)-1])

