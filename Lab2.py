#Lab-2: Write a function that returns all the permutation of the given string of length 3.

word = input('Enter three letter word : ')

result = []
for i in range(len(word)):
    for j in range(len(word)):
        if j==i:
            continue
        for k in range(len(word)):
            if  j==k or i==k:
                continue
            result.append(word[i]+word[j]+word[k])

print('All letter permutations of the XYZ are : ')            
print(result)