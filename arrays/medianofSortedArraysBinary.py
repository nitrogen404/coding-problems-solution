# O(log(m + n)) time
# O(1) space

def findMedian(array1, array2):
    if len(array1) > len(array2):
        return findMedian(array2, array1)

    lenA = len(array1)
    lenB = len(array2)
    low = 0
    high = lenA

    while low <= high:
        partX = (low + high) // 2
        partY = (lenA + lenB + 1) // 2 - partX

        maxLeftA = array1[partX - 1] if partX != 0 else float('-inf')
        minRightA = array1[partX] if partX == lenA else float('inf')

        maxLeftB = array2[partY - 1] if partY != 0 else float('-inf')
        minRightB = array2[partY] if partY == lenB else float('inf')

        if maxLeftA <= minRightB and maxLeftB <= minRightA:
            if (lenA + lenB) % 2 == 0:
                print(max(maxLeftA, maxLeftB), max(minRightA, minRightB))
                return (max(maxLeftA, maxLeftB) +
                        max(minRightA, minRightB)) // 2
            else:
                return max(maxLeftA, maxLeftB)
        elif maxLeftA > minRightB:
            high = partX - 1
        else:
            low = partX + 1
