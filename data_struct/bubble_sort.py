def bubble_sort(nums): 
	for i in range(len(nums)-1): #并不需要n趟， 只需要n-1趟。 只剩一个元素的时候可以直接返回
		for j in range(len(nums)-1-i):  #注意不要取nums[j+1]时下标不要超出范围
			if nums[j] > nums[j+1]:
				nums[j],nums[j+1] = nums[j+1],nums[j]
		print(nums)
	return nums 


a = [8,6,5,3,2,7,1]
b = [1]
c = []

print(bubble_sort(a))
print(bubble_sort(b))
print(bubble_sort(c))

