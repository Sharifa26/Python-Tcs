tim = '00:06'
print(tim)

def time(tim):
    arr= tim.split(':')


    if(int(arr[0]) > 12):
        m='PM'
    else:
        m='AM'
    
    if(int(arr[0]) == 0):
        arr[0]= 12
    if(int(arr[0]) > 12):
        arr[0]= int(arr[0]) - 12
    else: 
        arr[0]=arr[0]
    
    return (f'{arr[0]}:{arr[1]}  {m}')

time(tim)