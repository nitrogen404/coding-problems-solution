# O(n) time
# O(1) space
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentLen = 0
        maxLen = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                currentLen += 1
            else:
                currentLen = 0
            maxLen = max(currentLen, maxLen)
        return maxLen
