# O(NlogN + MlogM) time
# O(1) space

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    firstPointer = 0
    secondPointer = 0
    pair = []
    currentDiff = float("inf")
    smallest = float("inf")
    while firstPointer < len(arrayOne) and secondPointer < len(arrayTwo):
        firstNum = arrayOne[firstPointer]
        secondNum = arrayTwo[secondPointer]
        if firstNum == secondNum:
            return [firstNum, secondNum]
        elif firstNum < secondNum:
            currentDiff = secondNum - firstNum
            firstPointer += 1
        elif secondNum < firstNum:
            currentDiff = firstNum - secondNum
            secondPointer += 1
        if smallest > currentDiff:
            smallest = currentDiff
            pair = [firstNum, secondNum]
    return pair
