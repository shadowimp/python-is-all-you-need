def merge_sort(nums):
    if len(nums) <2: return nums

    mid = len(nums)//2
    left = merge_sort(nums[:mid])  # 将数组不断地拆分，递归使函数从最底部一个元素的时候进行操作
    right = merge_sort(nums[mid:])

    return merge(left,right)

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

