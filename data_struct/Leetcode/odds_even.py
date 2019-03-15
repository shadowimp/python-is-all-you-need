#-*-coding:utf-8-*-
#使数组的奇数在前，偶数在后。
def odds_even(nums) : 
	i,j = 0,len(nums)-1 

	while (i<j):
		if nums[i]%2==0 and nums[j]%2==1 :
			nums[i],nums[j]= nums[j],nums[i]
			i = i + 1
			j = j - 1 
		elif nums[i]%2==1 and nums[j]%2 ==1: 
			i = i + 1   
		elif nums[i]%2==0 and nums[j]%2 == 0: 
			j = j - 1 
		else: 
			i = i + 1
			j = j - 1

	return nums 

A = [4,3,1,2,4,7,5,3,8,2,4,6]
print(odds_even(A))