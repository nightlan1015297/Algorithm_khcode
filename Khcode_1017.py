import sys
while True:
	for i in range(1):
		data1 = sys.stdin.readline()
		data2 = sys.stdin.readline()
	data1 = data1.split(" ")
	data2 = data2.split(" ")
	data1 = list(map(int,data1))
	data2 = list(map(int,data2))
	ans = []
	for num2 in data2[1:]:
			for num1 in data1[1:]:
				ansnum=int(num1)*int(num2) 
				ans.append(ansnum)
				if len(ans) == data1[0]:
					for ansindex in range(0,len(ans)-1):
						print(ans[ansindex],end = " ")
					print(ans[len(ans)-1])
					ans=[]
