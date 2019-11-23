import sys
for stRS in sys.stdin:
	up = 0
	lo = 0
	for STR in stRS:
		if STR.isupper():
			up =up+1
		elif STR.islower():
			lo =lo+1
	print(lo , up)