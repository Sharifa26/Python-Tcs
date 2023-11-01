"""Input : 20
Output: 1 2 4 5 10 20
Explanation: 20 is completely 
divisible by 1, 2, 4, 5, 10 and 20.
"""


n=10
def print_divisors(n):
    for i in range(1,n+1):
            if( n % i == 0):
                print(i,end=" ")
print(print_divisors(n))
""" 
divisors = []
        for i in range(1, int(N**0.5)+1):
            if N % i == 0:
                divisors.append(i)
                if i!=N/i:
                    divisors.append(N//i)
        for i in range(len(divisors)): 
            print(sorted(divisors)[i], end=" ")
"""
# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true

# decimal = str(i).rjust(width)
# octal = oct(i)[2:].rjust(width)
# hexadecimal = hex(i)[2:].rjust(width).upper()
# binary = bin(i)[2:].rjust(width)
# print(decimal,octal,hexadecimal,binary)