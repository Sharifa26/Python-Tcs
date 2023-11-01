"""Input: N = 153
Output: "Yes"
Explanation: 153 is an Armstrong number
since 13 + 53 + 33 = 153.
Hence answer is "Yes".
"""

n=153

def arstrong(n):
    sum =0
    n=str(n)
    l=len(n)
    for i in range(l):
        sum += pow(int(n[i]),l)
    if(sum == int(n)):
        return "Yes"
    else:
        return "No"
    
print(arstrong(n))