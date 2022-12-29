#O(n) time
# O(1) space
def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            if height[0] == height[1]:
                return height[0] * height[1]
            
            return (abs(height[1] - height[0])) * min(height[1], height[0])

        maxArea = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            maxArea = max(maxArea, area)
            if height[left] < height[right]:
                left += 1
            elif height[right] < height[left]:
                right -= 1
            else:
                right -= 1
        return maxArea
