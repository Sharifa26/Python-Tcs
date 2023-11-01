# https://practice.geeksforgeeks.org/problems/fibonacci-to-n0811/1

def nFibonacci(N):
        arr=[0,1]
        a=0
        while a<=N:
            a=arr[-1]+arr[-2]
            if a>N:
                break
            arr.append(a)
        return arr


N=7
print(nFibonacci(N))