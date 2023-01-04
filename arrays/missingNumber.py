# O(n) time
# O(1) space
def missingNumber(self, nums: List[int]) -> int:
        actualSum = 0 
        for i in range(len(nums) + 1):
            actualSum += i
        return actualSum - sum(nums)
