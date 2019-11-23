import sys
for stRS in sys.stdin:
	ans =""
	for STR in stRS:
		if STR.isupper():
			ans =ans+STR.lower() 
		elif STR.islower():
			ans =ans+STR.upper() 
	print(ans)