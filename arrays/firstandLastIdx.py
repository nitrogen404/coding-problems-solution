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

       
# Sliding window method (bit more complicated)
# O(n) time O(n) space

def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums) and nums[i] != target:
            i += 1
        start = end = i
        if end == len(nums):
            return [-1, -1]
        else:
            for i in range(start, len(nums)):
                if nums[i] != target:
                    break
                else:
                    end += 1
            return [start, end - 1]
