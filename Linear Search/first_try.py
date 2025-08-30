"""
Problem statement
You are given an array ‘arr’ containing ‘n’ integers. You are also given an integer ‘num’, and your
 task is to find whether ‘num’ is present in the array or not.


If ‘num’ is present in the array, return the 0-based index of the first occurrence of ‘num’. 
Else, return -1.

Example:
Input: ‘n’ = 5, ‘num’ = 4 
'arr' =  [6,7,8,4,1] 
Output: 3
Explanation:
4 is present at the 3rd index.
"""

def linearSearch(n: int, num: int, arr: list) -> int:
    # Write your code here.
    # n -> length of the array , num is int , arr is the array 
    for i in range(0,n):
        if arr[i] == num:
            return i
    return -1
    

arr = [1,2,3,4,5,6,7,8,9,0]
print(linearSearch(len(arr),10,arr))
print(linearSearch(len(arr),0,arr))
