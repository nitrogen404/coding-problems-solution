# O(n) time 
# O(1) space
def longestPeak(array):
    maxLength = 0
    i = 1
    while i < len(array) - 1:
        peak = array[i - 1] < array[i] and array[i + 1] < array[i]
        if not peak:
            continue
        leftIdx = i - 2
        while leftIdx >= 0 and array[leftIdx + 1] > array[leftIdx]:
            leftIdx -= 1
        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx - 1] > array[rightIdx]:
            rightIdx += 1
        currentLength = rightIdx - leftIdx - 1
        maxLength = max(currentLength, maxLength)
        i = rightIdx
    return maxLength
