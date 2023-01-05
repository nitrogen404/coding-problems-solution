# O(n) time
# O(1) space

class Solution:
    def jump(self, nums: List[int]) -> int:
        result = l = r = 0

        while r < len(nums) - 1:
            maxDistance = 0
            for i in range(l, r + 1):
                maxDistance = max(maxDistance, i + nums[i])
            l = r + 1
            r = maxDistance
            result += 1
        return result
