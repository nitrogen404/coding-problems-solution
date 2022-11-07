# O(logn) time
# O(1) space
def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            middleElement = (start + end) // 2
            if target == nums[middleElement]: return middleElement
            elif target > nums[middleElement]:
                start = middleElement + 1
            else:
                end = middleElement - 1
        return end + 1
