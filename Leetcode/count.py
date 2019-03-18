#-*-coding:utf-8-*-

'''
得到一个数组中各个元素的个数。
输入： 一个数组
输出： 一个字典

'''
def get_counts(nums): 
	counts = {} #创建一个空字典用来存放数组中的元素及其个数。
	for x in nums:  
		if x in counts:  #遍历字典的key，看其中是否有x元素，如果有给x对应的value加一。否则创建一个value值为一。
			counts[x] += 1   
		else: 
			counts[x] = 1
	return counts


nums = [4,4,3,2,5,56,5]
print(get_counts(nums))