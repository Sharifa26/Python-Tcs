"""Input:
N = 1004
Output: 1554
Explanation: There are two zeroes in 1004
on replacing all zeroes with "5", the new
number will be "1554".
"""

def convertFive(n):
    # Code here
    x=str(n)
    x=x.replace('0','5')
    n=int(x)
    return n

n=1004
print(convertFive(n))