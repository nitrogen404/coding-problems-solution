# O(n) time
# O(1) space
def findThreeLargestNumbers(array):
    result = [None, None, None]
    for num in array:
        updateLargest(result, num)
    return result

def updateLargest(result, num):
    if result[2] is None or num > result[2]:
        shiftUpdate(result, num, 2)
    elif result[1] is None or num > result[1]:
        shiftUpdate(result, num, 1)
    elif result[0] is None or num > result[0]:
        shiftUpdate(result, num, 0)

def shiftUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]
