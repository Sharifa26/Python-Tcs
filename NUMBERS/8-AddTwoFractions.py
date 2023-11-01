"""
Input
1
1 500 2 500
Output
3/500
"""
def addFraction(num1, den1, num2, den2):
    #Code here
    from fractions import Fraction
    n=(num1*den2)+(num2*den1)
    d=den1*den2
    return(str(Fraction(n,d)))


num1=1
den1=500
num2=2
den2=500
print(addFraction(num1, den1, num2, den2))
