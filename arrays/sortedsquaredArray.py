# O(N) - time
# O(N) - Space
def sortedSquaredArray(array):
    resultantArray = [0] * len(array)
    endPointer = len(array) - 1
    startPointer = 0
    tempPointer = len(array) - 1
    while endPointer != startPointer:
        if abs(array[endPointer]) > abs(array[startPointer]):
            resultantArray[tempPointer] = array[endPointer] ** 2
            endPointer -= 1
            tempPointer -= 1
        elif abs(array[endPointer]) <= abs(array[startPointer]):
            resultantArray[tempPointer] = array[startPointer] ** 2
            startPointer += 1
            tempPointer -= 1
    resultantArray[tempPointer] = array[startPointer] ** 2
    return resultantArray
    
