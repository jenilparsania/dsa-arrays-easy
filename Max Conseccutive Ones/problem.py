"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
"""

def findMaxConsecutiveOnes(nums):
    n = len(nums)
    now = 0
    most = 0

    for i in range(0,n):
        if nums[i]==1:
            now +=1
        else:
            most = max(most,now)
            now = 0
    if now > most:
        return now
        
    return most
        
nums = [1,1,0,1,1,1]
nums2 = [1,1,1,1,1,0,0,0,0,1,1,0]
print(findMaxConsecutiveOnes(nums))
print(findMaxConsecutiveOnes(nums2))