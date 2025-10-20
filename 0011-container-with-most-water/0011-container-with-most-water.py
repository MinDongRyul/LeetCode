class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_ = 0
        while left < right:
            if height[left] <= height[right]:
                max_ = max(max_, (right-left)*height[left])
                left += 1
            else:
                max_ = max(max_, (right-left)*height[right])
                right -= 1
        return max_