# O(n) time 
# O(1) space
def searchMatrix(matrix, target):
        for row in matrix:
            if row[0] <= target and target <= row[len(row) - 1]:
                return binarySearch(row, target)
             

def binarySearch(array, target):
    l = 0 
    h = len(array) - 1
    
    while l <= h:
        mid = (l + h) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            h = mid - 1
        else:
            l = mid + 1
    return False


print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 40))
