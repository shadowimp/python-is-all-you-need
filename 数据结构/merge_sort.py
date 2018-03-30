#-*-coding:utf-8-*-
def merge_sort(nums):
	if len(nums) >1 :  #如果数组只有一个元素或者没有元素，最后就会return数组本身
		mid = len(nums)//2 
		left = merge_sort(nums[:mid])   # 将数组拆分 ， 递归使函数从最底部一个元素的地方进行操作
		right = merge_sort(nums[mid:]) 

		i,j,k = 0,0,0 	
		while i<len(left) and j<len(right):  #left 和right 作比较 将较大元素给nums
			if left[i] < right[j]: 
				nums[k] = left[i] 
				i = i+1 
			else: 
				nums[k] = right[j] 
				j = j+1 
			k = k+1 

		while i<len(left):    # 如果最后有剩余的元素，将其直接附加在nums的后面
			nums[k] = left[i]
			i = i+1
			k = k+1 
		while j <len(right):
			nums[k] = right[j] 
			j = j+1 
			k = k+1
	return nums

a = [3,5,1,8,2,9] 
b = [1]
print(merge_sort(a))
print(merge_sort(b))
