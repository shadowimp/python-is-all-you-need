def bubble_sort(nums): 
	for i in range(len(nums)-1):
		for j in range(len(nums)-1-i):
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

