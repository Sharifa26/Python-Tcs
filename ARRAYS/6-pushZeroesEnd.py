arr = [3, 5, 0, 0, 4]
n=len(arr)


def pushZerosToEnd(arr, n):
    count=0
    for i in range(n):
        if arr[i]!=0:
            arr[count]=arr[i]
            count+=1
    while count < n:
        arr[count]=0
        count+=1
    return arr


print(pushZerosToEnd(arr, n))

# 4