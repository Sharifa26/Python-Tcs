# https://practice.geeksforgeeks.org/problems/find-the-smallest-and-second-smallest-element-in-an-array3226/1

def minAnd2ndMin( a, n):
    #code here
    arr = list(set(a))
    arr.sort()
    if len(arr)<=1:
        return [-1,-1]
    return arr[:2]

a=[1,2,1,3,6,0]
n=len(a)

print(minAnd2ndMin( a, n))
