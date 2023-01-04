# O(n2) time
# o(1) space

class Solution:
    def rotate(self, nums: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                nums[i][j], nums[j][i] = nums[j][i], nums[i][j]
    
        for row in nums:
            row.reverse()
