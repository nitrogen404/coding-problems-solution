def twoNumberSum(array, targetSum):
    
    array.sort()
    leftPointer = 0
    rightPointer = len(array) - 1
    while leftPointer < rightPointer:
        currentSum = array[leftPointer] + array[rightPointer]
        if currentSum == targetSum:
            return [array[leftPointer], array[rightPointer]]
        elif currentSum < targetSum:
            leftPointer += 1
        elif currentSum > targetSum:
            rightPointer -= 1
    return []

