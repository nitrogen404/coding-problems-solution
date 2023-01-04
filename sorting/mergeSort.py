# O(nlogn) time N space for each level and logn for dividing
# O(nlogn) space 
def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        leftSubarray = array[:mid]
        rightSubarray = array[mid: ]
        mergeSort(leftSubarray)
        mergeSort(rightSubarray)

        i = j = k = 0
        while i < len(leftSubarray) and j < len(rightSubarray):
            if leftSubarray[i] < rightSubarray[j]:
                array[k] = leftSubarray[i]
                i += 1
            else:
                array[k] = rightSubarray[j]
                j += 1
            k += 1
            
        while i < len(leftSubarray):
            array[k] = leftSubarray[i]
            i += 1
            k += 1
        while j < len(rightSubarray):
            array[k] = rightSubarray[j]
            j += 1
            k += 1
    return array
