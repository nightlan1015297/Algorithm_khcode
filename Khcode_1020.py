import sys
while True:
	nums = []
	num = int(sys.stdin.readline())
	for i in range(1,int(num**0.5)+1):
		if num % i == 0:
			if int(num/i) == i :
				nums.append(i)
			else:	
				nums.append(i)
				nums.append(int(num / i))
	nums.sort(reverse=False)
	for ind in range(len(nums)-1):
		print(nums[ind] , end =" ")
	print(nums[len(nums)-1])	