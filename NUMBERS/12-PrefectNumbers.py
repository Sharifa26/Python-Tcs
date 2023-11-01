"""Input:
N = 6
Output:
1 
Explanation:
Factors of 6 are 1, 2, 3 and 6.
Excluding 6 their sum is 6 which
is equal to N itself. So, it's a
Perfect Number.
"""



def isPerfectNumber(N):
        # code here 
        # if(N==6 or N==28 or N==496 or N==8128 or N==33550336 or N==8589869056 or N==137438691328):
        #     return 1
        # else:
        #     return 0

        if N <= 1:
            return 0
        sum = 1 
        i = 2
        while i * i <= N:
            if N % i == 0:
                sum += i + N / i
            i += 1
        if sum == N: 
            return 1 
        else: 
            return 0
        
N=6
print(isPerfectNumber(N))