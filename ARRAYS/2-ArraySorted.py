# https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1

"""
Input:
N = 5
arr[] = {10, 20, 30, 40, 50}
Output: 1
Explanation: The given array is sorted.
"""
N = 5
arr = [10, 20, 30, 40, 50]
def arraySortedOrNot(arr, N):
    if(arr == sorted(arr)):
        return True
    else:
        return False
    
print(arraySortedOrNot(arr, N))



# sample