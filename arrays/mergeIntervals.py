# O(n) time 
# O(n) space
class Solution:
    def merge(self, array: List[List[int]]) -> List[List[int]]:
        array.sort(key = lambda i: i[0])
        result = []
        currentInterval = array[0]
        for interval in array:
            if interval[0] <= currentInterval[1]:
                currentInterval[1] = max(interval[1], currentInterval[1])
            else:
                result += [currentInterval]
                currentInterval = interval
        result += [currentInterval]
        return result
