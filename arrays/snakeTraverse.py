# O(n*m) time 
# O(n) space
def spiralTraverse(array):
    result = []
    pointer = 0
    for subarr in array:
        if pointer == 0:
            for i in range(len(subarr)):
                result += [subarr[i]]
                pointer += 1
        else:
            while pointer != 0:
                result += [subarr[pointer - 1]]
                pointer -= 1
    return result
