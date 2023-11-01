"""Input: 5
Output: 9 6
Explanation: Odd numbers upto 5 are 1, 3, 5
and their sum = 1 + 3 + 5 = 9.Even numbers
upto 5 are 2 and 4 and their sum = 2 + 4 = 6.
"""

def find_sum(n):
		# Code here
# 		even=0
# 		odd=0
# 		for i in range(1,n+1):
# 		    if(i%2==0):
# 		        even +=i
# 		    else:
# 		        odd +=i
# 		return [odd,even]

        # sums=(n*(n+1))/2
        # even=(n/2)*(n/2+1)
        # return [sum-even,even]
        
        nev = n//2
        nod = n-n//2
        return [nod**2,nev*(nev+1)]

n=5
print(find_sum(n))