import sys
for numbers in sys.stdin:
	numlist = numbers.split(" ")
	if len(numlist) > 1:
		minima = int(numlist[0])
		for number in numlist:
			if int(number) < int(minima):
				minima = number
		print(minima)


