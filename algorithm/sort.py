def InsertSort(nums):
	for i in range (len(nums)):
		j = i
		while (j>0):
			if nums[j]<nums[j-1]:
				nums[j],nums[j-1]= nums[j-1],nums[j]
			j = j - 1
	return nums

print(InsertSort([6,4,5,1,7,3]))


def BubbleSort(nums):
	for i in range(len(nums),0,-1):
		j = 1 
		while(j<i):
			if nums[j-1]>nums[j]:
				nums[j],nums[j-1]= nums[j-1],nums[j]
			j = j + 1
	return nums

print(BubbleSort([6,4,5,1,7,3]))

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

# merge_sort 
def merge_sort(nums):
    if len(nums)<=1: 
        return nums
    mid = len(nums)//2
    nums1 = merge_sort(nums[:mid])  # 将数组不断地拆分，递归使函数从最底部一个元素的时候进行操作
    nums2 = merge_sort(nums[mid:])
    return merge(nums1,nums2)

def merge(nums1,nums2):
    """
    合并两个有序的数组，产生一个新的有序数组
    """
    nums3 = []
    i ,j = 0,0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            nums3.append(nums1[i])
            i += 1
        else:
            nums3.append(nums2[j])
            j += 1
    nums3 += nums1[i:] #多余的元素直接加到结果的后面
    nums3 += nums2[j:]
    return nums3

print(merge_sort([8,2,3,5,7,6,1,4]))


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
print(quick_sort([6,4,5,1,7,3]))


def quick_sort(list):

	if len(list) <= 2 :
		return list 

	pivot = list[0]

	less= []
	greater = []

	for i in list[1:]:
		if i < pivot :
			less.append(i)
		else:
			greater.append(i)

	return quick_sort(less) + [pivot] + quick_sort(greater)
 
A = [2,5,3,6,1,8,3]
print(quick_sort(A))


def quicksort(arr): 
	if len(arr)<=1 : 
		return arr 

	pivot = arr[len(arr)//2]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x==pivot]
	right = [x for x in arr if x>pivot] 
	return quicksort(left)+ middle + quicksort(right) 

B = [2,5,3,6,1,8,3]
C = [2,1]
print(quicksort(B))
print(quicksort(C))


def  quick(nums): 
	if len(nums)<=1: 
		return nums 
	pivot = nums[len(nums)//2 ]
	left = [x for x in nums if x<pivot]
	middle = [x for x in nums if x == pivot] 
	right = [x for x in nums if x> pivot]
	return quick(left) +  middle + quick(right)

def qsort(nums):
	if len(nums)<=1: 
		return nums 
	return qsort([x for x in nums if x<nums[0]]) + [x for x in nums if x == nums[0]] + qsort([x for x in nums if x>nums[0]])
print(qsort([6,4,5,1,7,3]))

