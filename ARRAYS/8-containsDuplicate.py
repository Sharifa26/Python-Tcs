# https://leetcode.com/problems/contains-duplicate/submissions/
nums = [1,2,3,1]

def contains(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
        
print(contains(nums))