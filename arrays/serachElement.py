# O(logn) time
# O(1) space
def searchElement(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        if array[low] <= array[mid]:  # check if left part is sorted
            if array[low] <= target and target <= array[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:  # check if the right part is sorted
            if array[mid] >= target and target <= array[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1
