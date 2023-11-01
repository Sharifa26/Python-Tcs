"""Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

def climb(n):
    prev = 1
    prev2=0
    for i in range(1,n+1):
        cur = prev+prev2
        prev2=prev
        prev=cur
    return prev

n=3
print(climb(n))