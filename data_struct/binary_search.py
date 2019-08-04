def binary_search(nums,x):
	left,right = 0, len(nums)-1

	while(left<=right):  #left == right时 就是数组中仅剩一个元素，mid==left==right 其必然被返回
		mid = (left + right)//2
		if nums[mid] == x :
			return mid
		elif nums[mid] > x :
			right = mid -1
		else :
			left = mid + 1

	return None


test_list = [2,5,7,9,10,23]
print(binary_search(test_list,23))


def binary_search_recursion(nums,x,left,right):
	mid = left + (right-left)//2
	if nums[mid] == x :
		return mid
	elif nums[mid] > x :
		return binary_search_recursion(nums,x,left,mid-1)
	else:
		return binary_search_recursion(nums,x,mid+1,right)

print(binary_search_recursion(test_list,23,0,5))
