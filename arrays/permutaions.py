# O(n) time 
# O(1) space

class Solution:
    def __init__(self):
        self.result = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, [])
        return self.result
    
    def backtrack(self, nums, path):
        if len(nums) == 0:
            self.result.append(path)
        
        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i + 1:], path + [nums[i]])
