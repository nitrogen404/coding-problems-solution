# O(nlogn) time 
# O(1) space
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        return self.mergeSort(nums)

    def mergeSort(self, nums):
        if len(nums) > 1:
            r = len(nums) // 2
            leftArr = nums[: r]
            rightArr = nums[r: ]
            self.mergeSort(leftArr)
            self.mergeSort(rightArr)

            i = j = k = 0
            while i < len(leftArr) and j < len(rightArr):
                if leftArr[i] <= rightArr[j]:
                    nums[k] = leftArr[i]
                    i += 1
                else:
                    nums[k] = rightArr[j]
                    j += 1
                k += 1
            while i < len(leftArr):
                nums[k] = leftArr[i]
                i += 1
                k += 1
            while j < len(rightArr):
                nums[k] = rightArr[j]
                j += 1
                k += 1
        return nums
