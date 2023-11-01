nums = [1,2,3,1]

def contains(nums):
    n=len(nums)
    for i in range(n-1):
        for j in range(i+1,n):
            if(nums[i] == nums[j]):
             return True
    return False
        
print(contains(nums))