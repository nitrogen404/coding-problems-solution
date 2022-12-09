# O(n) time 
# O(1) space

def multiplyArray(array):
    result = [1] * len(array)
    prefix = 1
    for i in range(len(array)):
        result[i] = prefix
        prefix *= array[i]
    postfix = 1
    for i in range(len(array) - 1, -1, -1):
        result[i] = postfix * result[i]
        postfix *= array[i]
    return result
