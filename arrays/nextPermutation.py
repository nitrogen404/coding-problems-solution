# O(n) time 
# O(1) space

if len(array) <= 1: 
        return array
    
    i, j = len(array) - 1
    while i > 0 and array[i - 1] >= array[i]:
        i -= 1
    
    if i == 0:
        return array.reverse()
    
    k = i - 1
    while array[j] <= array[k]:
        j -= 1
    array[k], array[j] = array[j], array[k]
    l = k + 1
    r = len(array) - 1
    while l < r:
        array[l], array[r] = array[r], array[l]
        l += 1
        r -= 1
    return array
