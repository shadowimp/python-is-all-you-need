# https://leetcode.com/problems/two-sum/
# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

# <script>
# /**
#  * @param {number[]} nums
#  * @param {number} target
#  * @return {number[]}
#  */
# var twoSum = function(nums, target) {
#     numsLength = nums.length;
#     for (var i = 0; i < numsLength; i++) {
#         for (var j = i+1; j < numsLength; j++) {
#             if (nums[i]+nums[j] == target){
#                 return [i,j];
#             }
#         }
#     }
# };

# console.log(twoSum([2,8,3,8,1],10));

# </script>

class Solution(object):
    """
    Solution 1 31%
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = nums[:]	# keep the input list intact
        while len(nums):
            spot = target - nums.pop()
            # ([1,10,8,13,25,2], 27),

            if spot in nums:
                break

        index1 = nums.index(spot)
        index2 = len(nums)

        return [index1 + 1, index2 + 1]

# score
# Your runtime beats 31.77% of python submissions.



# solution 2
class Solution2(object):
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

import time

# test function
def test(numsTargetPairs, obj):
    for pair in numsTargetPairs:
        nums, target = pair
        start = time.time()

        # run core funciton
        results = obj.twoSum(nums, target)

        end = time.time()
        print(end - start)
        print("%d + %d = %d" % (nums[results[0] - 1], nums[results[1] - 1], target) )

# test run
pairs = [
	([1,10,8,13,25,2], 27),
	([0,1,2,0], 0),
	([4,1,2,4,2], 8),
	([3,2,4], 6),
	([1,2,3,4,5], 8),
	([-1,-2,-3,-4,-5], -8),
]



s1 = Solution()
print(s1.__doc__)
test(pairs, s1)


s2 = Solution2()
print(s2.__doc__)
test(pairs, s2)
