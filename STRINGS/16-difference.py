# https://leetcode.com/problems/find-the-difference/description/

"""
Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.
Example 2:

Input: s = "", t = "y"
Output: "y"
"""

def findTheDifference(s, t):
    c = 0
    for cs in s: c ^= ord(cs) #ord is ASCII value
    for ct in t: c ^= ord(ct)
    return chr(c)

s = "abcd"
t = "abcde"

print(findTheDifference(s,t))