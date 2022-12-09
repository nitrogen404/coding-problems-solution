# O(logn) time
# O(n) space
 def searchRange(self, nums: List[int], target: int) -> List[int]:
        # [5, 8, 8, 8, 8, 10]
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        return [left, right]
        

    def binarySearch(self, nums, target, bias):
        low, high = 0, len(nums) - 1
        i = -1

        while low <= high:
            mid = (low + high) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                i = mid
                if bias:
                    high = mid - 1
                else:
                    low = mid + 1
        return i
