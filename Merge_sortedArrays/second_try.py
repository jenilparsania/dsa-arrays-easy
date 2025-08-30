#  the two a and b arrays would be sorted 


def sortedArray(a: list, b: list) -> list:
    # Write your code here
    answer = []
    i = 0
    j = 0
    while i<len(a) and j<len(b):
        if a[i]<= b[j]:
            answer.append(a[i])
            i+=1
                
        else:
            answer.append(b[j])
            j+=1
    
    while i<len(a):
            answer.append(a[i])
            i+=1
       

    while j<len(b):
            answer.append(b[j])
            j+=1

    #  also have to remove the duplicates
    merged= []
    for x in range(0,len(answer)):
         if answer[x] not in merged:
              merged.append(answer[x])


         
       

    return merged


a = [2,8,9,10,11] 
b = [1,2,3,4,5]

print(sortedArray(a,b))

