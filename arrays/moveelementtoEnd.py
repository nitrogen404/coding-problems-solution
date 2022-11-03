# O(n) time
# O(1) space
def moveElementToEnd(array, toMove):
    rightPointer = len(array) - 1
    leftPointer = 0
    while leftPointer < rightPointer:
        while leftPointer < rightPointer and array[rightPointer] == toMove:
            rightPointer -= 1
        if array[leftPointer] == toMove:
            array[rightPointer], array[leftPointer] = array[leftPointer], array[rightPointer]
        leftPointer += 1
    return array
    
