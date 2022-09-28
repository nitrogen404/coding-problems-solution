# O(n^2) time 
# O(n) space

def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        leftPointer = i + 1
        rightPointer = len(array) - 1
        while leftPointer < rightPointer:
            currentSum = array[i] + array[leftPointer] + array[rightPointer]
            if currentSum == targetSum:
                triplets.append([array[i], array[leftPointer], array[rightPointer]])
                leftPointer += 1
                rightPointer -= 1 
            elif currentSum < targetSum:
                leftPointer += 1
            elif currentSum > targetSum:
                rightPointer -= 1
    return triplets
