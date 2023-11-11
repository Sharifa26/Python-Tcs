arr=[11, 12, 22, 25, 10, 64, 90]

def bubble(arr):
    n=len(arr)

    swaped = False

    for i in range(n-1):

        for j in range(n-i-1):

            if arr[j] > arr[j+1]:
                swaped = True
                arr[j],arr[j+1] = arr[j+1],arr[j]
            
        if not swaped:
            return 
    return arr


print(bubble(arr))