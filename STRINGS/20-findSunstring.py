"""
https://practice.geeksforgeeks.org/problems/implement-strstr/1

Input:
s = GeeksForGeeks, x = For
Output: 5
Explanation: For is present as substring
in GeeksForGeeks from index 5 (0 based
indexing).

Input:
s = GeeksForGeeks, x = Fr
Output: -1
Explanation: Fr is not present in the
string GeeksForGeeks as substring.
"""

def strstr(s,x):
    return s.find(x)

s ="GeeksForGeeks"
x = "Fr"
print(strstr(s,x))