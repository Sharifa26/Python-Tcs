def printFibb(n):
    if n>1:
        arr=[1,1]
        for i in range(2,n):
            arr.append(arr[-1]+arr[-2])
        return arr
    elif n==1:
        return [1]
    else:
        return [-1]
    
n=7
print(printFibb(n))