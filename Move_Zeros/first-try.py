"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order 
of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""

def moveZeros(arr:list):
    arr.sort()
    
    i = 0
    while(arr[i]==0):
        i+=1

    arr[:] = arr[i:] + arr[0:i]  # arr[included:included+1]
    return arr,i


arr = [0,1,0,3,12]   # would throw an error at [0,0]
print(moveZeros(arr))