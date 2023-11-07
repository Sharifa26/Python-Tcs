# https://practice.geeksforgeeks.org/problems/count-alphabets3649/1

"""
Input:
S = "adjfjh23"
Output: 6
Explanation: only last 2 are not 
alphabets.
"""
S = "adjjh23"
def Count(S):
    # code here
    count =0
    for i in S:
        if( i.isalpha() == True):
            count +=1
    return count

print(Count(S))