def InsertSort(nums):
	for i in range (len(nums)):
		j = i
		while (j>0):
			if nums[j]<nums[j-1]:
				nums[j],nums[j-1]= nums[j-1],nums[j]
			j = j - 1
	return nums

print InsertSort([6,4,5,1,7,3])


def BubbleSort(nums):
	for i in range(len(nums),0,-1):
		j = 1 
		while(j<i):
			if nums[j-1]>nums[j]:
				nums[j],nums[j-1]= nums[j-1],nums[j]
			j = j + 1
	return nums

print BubbleSort([6,4,5,1,7,3])


def MergeSort(nums):
	if len(nums)<=1 :
		return nums
	middle = len(nums)//2
	left = MergeSort(nums[:middle])
	right = MergeSort(nums[middle:])

	return merge(left,right)

def merge(left,right):
	merged = []
	i , j = 0, 0
	left_len , right_len = len(left),len(right)
	while i<left_len and j<right_len:
		if left[i] <= right [j]:
			merged.append(left[i])
			i = i+1 
		else: 
			merged.append(right[j])
			j = j+1
	merged.extend(left[i:])
	merged.extend(right[j:])
	return merged

print MergeSort([6,4,5,1,7,3])


print('*'*30)
print ("quick_sort:")
def quick_sort(nums):
	if len(nums)<2 : 
		return nums 
	pivot = nums[0] 
	left = [x for x in nums if x<pivot]
	middle = [x for x in nums if x==pivot]
	right = [x for x in nums if x>pivot]
	return quick_sort(left)+ middle + quick_sort(right)
print quick_sort([6,4,5,1,7,3])

