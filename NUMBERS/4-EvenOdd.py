"""Input: 
N1 = "12"
N2 = "15"
Output: 1
Explanation: 12 * 15 = 180 which is an 
even number.
"""
def EvenOdd(n1, n2):
        # code here
        s=int(n1)*int(n2)
        if(s%2==0):
            return 1
        else:
            return 0
        
n1="12"
n2="15"
print(EvenOdd(n1,n2))