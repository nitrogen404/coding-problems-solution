# O(N) time
# O(N) space
class Solution:
    def findMedianSortedArrays(self, array1: List[int], array2: List[int]) -> float:
        mergedArr = []
        firstPointer = 0
        secondPointer = 0
        while firstPointer < len(array1) and secondPointer < len(array2):
            if array1[firstPointer] < array2[secondPointer]:
                mergedArr.append(array1[firstPointer])
                firstPointer += 1
            elif array1[firstPointer] > array2[secondPointer]:
                mergedArr.append(array2[secondPointer])
                secondPointer += 1
            elif array1[firstPointer] == array2[secondPointer]:
                mergedArr.append(array1[firstPointer])
                mergedArr.append(array2[secondPointer])
                firstPointer += 1
                secondPointer += 1

        if firstPointer < len(array1):
            mergedArr += array1[firstPointer:]
        if secondPointer < len(array2):
            mergedArr += array2[secondPointer:]
        
        middleIdx = len(mergedArr) // 2
        if len(mergedArr) % 2 == 0:
            
            return (mergedArr[middleIdx] + mergedArr[middleIdx - 1]) / 2
        else:
            
            return mergedArr[middleIdx]
