#-*-coding:utf-8-*-

'''
Two Sum 一个数组中的两个数相加等于一个给定数，返回数组中两个数的下标。
输入： 一个数组，一个数字
输出： 两个数字

'''
def two_sum(nums,target): 
	nums_dict = {} #创建一个空字典,将target-num1作为key，num1的下标作为value。
	for i in range(len(nums)):  
		if nums[i] in nums_dict:  #遍历字典看其中是否有x，如果有说明两个数找到了
			return nums_dict[nums[i]],i
		else:  #如果没有，则将 target-nums1 : nums1的下标 存入字典nums_dict
			nums_dict[target-nums[i]] = i


nums = [4,3,2,5,9]
print(two_sum(nums,5))