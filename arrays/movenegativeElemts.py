# O(n) time
# O(1) space
def moveElements(array):
    j = 0
    for i in range(len(array)):
        if array[i] < 0:
            array[i], array[j] = array[j], array[i]
            j += 1
    return array
