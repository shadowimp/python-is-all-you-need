r# LeetCode

![python](https://img.shields.io/badge/python-3.5-ff69b4.svg)

算法练习

1.Two Sum 

    class Solution(object):
    """
    Solution 2 98%
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                # ([1,10,8,13,25,2], 27),
    
                buff_dict[target - nums[i]] = i

### 链接 

[知乎profile](https://www.zhihu.com/people/zhang-yuan-bo-76/activities)


    def twoSum(self,nums,target):
            if len(nums)<=1 :
                return nums
            buff_dict = {}
            for i in range(len(nums)): 
                if nums[i] in buff_dict: 
                    return [buff_dict[nums[i],i]
                else : 
                    buff_dict[target - nums[i]] = i 

