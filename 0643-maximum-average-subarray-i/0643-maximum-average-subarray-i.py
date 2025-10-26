class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_max = sum(nums[:k])
        max_sum = window_max
        
        for i in range(k, len(nums)):
            window_max += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_max)
        
        return max_sum / k