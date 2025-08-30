def missingNumber(nums:list):
    n = len(nums)
    for i in range(0,n+1):   
        if i not in nums:
            return i
    


nums = [0,1]
print(missingNumber(nums))

# I did for i in range(0,n): first but it was causing an error in the [0,1] because the length would
# be 2 and i would never go until 2 and 2 itself is the missing number , so None would be returned
# every time, so then I changed into n+1 and it would go for the last number as well 

            
