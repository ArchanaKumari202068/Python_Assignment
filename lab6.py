def find_duplicate(A):
    result= set([])
    
    for i in range (0,len(x)):
        for j in range(i+1,len(x)):
            if x[i]==x[j]:
                result.add(A[i])
    return result            
x = [1,2,3,4,2,7,7,4]
print(find_duplicate(x))