#  why this is not working (do not know)

def sortedArray(a: list, b: list) -> list:
    # Write your code here
    answer = []
    i = 0
    j = 0
    while i<len(a) and j<len(b):
        if a[i]<= b[j]:
            if a[i] not in answer:
                answer.append(a[i])
                i+=1
                
        elif b[j] not in answer:
            answer.append(b[j])
            j+=1
            
            

    while i<len(a):
        if a[i] not in answer:
                answer.append(a[i])
                i+=1
       

    while j<len(b):
        if b[j] not in answer:
                answer.append(b[j])
                j+=1
       

    return answer


a = [6,4,2,6,7] 
b = [1,2,3,4,5]

print(sortedArray(a,b))
