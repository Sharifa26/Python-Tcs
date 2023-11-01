# https://leetcode.com/problems/two-sum/

"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

nums = [2,7,11,15]
target = 9
def twoSum(nums, target):
    l = len(nums)
    for i in range(l-1):
        for j in range(i+1,l):
            if nums[i] + nums[j] == target:
                return [i,j]
    return[]

print(twoSum(nums, target))
# sample