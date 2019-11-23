import sys
while True:
	ans = ""
	Str = sys.stdin.readline().strip().split(" ")
	Str = list(map(int,Str))
	Str.sort(reverse = False)
	for word in Str:
		ans  = ans + str(word) + " "
	print(ans.strip())