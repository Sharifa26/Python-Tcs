nums = [4,1,2,1,2]

def single(nums):
    a=0
    for i in nums:
        a=a^i
    return a
    
print(single(nums))