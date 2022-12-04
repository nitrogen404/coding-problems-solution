# O(n) time 
# O(n) space
def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for idx in range(len(nums)):
            if nums[idx] in seen:
                return True
            seen.update({nums[idx]: idx})
        return False
