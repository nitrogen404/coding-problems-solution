# naive solution 
# O(n2) time 
# O(1) space

def firstDuplicateValue(array):
    defaultValue = -1
    minIdx = float("inf")
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                minIdx = min(j, minIdx)
    if minIdx != float("inf"):
        return array[minIdx]
    else:
        return defaultValue
        

# Optimal Solution
# O(n) time 
# O(1) space

def firstDuplicateValue(array):
    for value in array:
        absValue = abs(value)
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] *= -1
    return -1
    

