# https://www.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1

"""
Input:
str1 = aab
str2 = xxy
Output: 
1
Explanation: 
There are two different characters in aab and xxy, i.e a and b with frequency 2 and 1 respectively.
"""

def areIsomorphic(str1,str2):
    if len(str1) != len(str2):
        return 0
    d={}
    s={}
    for c1,c2 in zip(str1,str2):
        if(c1 in d and d[c1]!=c2) or (c2 in s and s[c2] != c1):
            return 0
        d[c1]=c2
        s[c2]=c1
    return 1


str1 = "aab"
str2 = "xyz"
print(areIsomorphic(str1,str2))