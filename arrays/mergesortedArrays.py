# O(m) time
# O(1) space

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        bigPointer = 0
        smallPointer = 0
        for i in range(len(nums2)):
            if nums1[bigPointer] < nums2[smallPointer]:
                bigPointer += 1
            else:
                nums1[bigPointer], nums2[smallPointer] = nums2[smallPointer], nums1[bigPointer]
                bigPointer += 1

        for i in range(len(nums2)):
            nums1[bigPointer] = nums2[i]
            bigPointer += 1
