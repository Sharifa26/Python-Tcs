"""N = 2021
Output:
0
Explanation:
2021 is not divisible by 100
and is also not divisible by 4
so its not a leap year
"""
def isLeap(N):
        # code here
        if (N%400==0) or (N%100!=0 and N%4==0):
            return 1
        return 0
N=2021
print(isLeap(N))