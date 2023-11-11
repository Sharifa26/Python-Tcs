arr = [-2, 45, 0, 11, -9,88,-97,-202,747,1]
n = len(arr)

def select(arr,n):
    for i in range(n):
        min_x =i
        for j in range(i+1,n):
            if(arr[j]<arr[min_x]):
                min_x=j
        arr[i],arr[min_x] =arr[min_x],arr[i]
    

    return arr

print(select(arr,n))