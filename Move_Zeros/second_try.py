def moveZeros(arr:list):
    arr.sort()
    
    i = 0
    for i in range(0,len(arr)):
        if arr[i]!=0:
            count = i
            break

    if count == len(arr):
        return arr
    

            

    arr[:] = arr[count:] + arr[0:count]  # arr[included:included+1]
    return arr


arr = [0,0]
print(moveZeros(arr))