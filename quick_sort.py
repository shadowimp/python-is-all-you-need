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
print quick_sort(A)


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
print quicksort(B)
print quicksort(C) 


def  quick(nums): 
	if len(nums)<=1: 
		return nums 
	pivot = nums[len(nums)//2 ]
	left = [x for x in nums if x<pivot]
	middle = [x for x in nums if x == pivot] 
	right = [x for x in nums if x> pivot]
	return quick(left) +  middle + quick(right)