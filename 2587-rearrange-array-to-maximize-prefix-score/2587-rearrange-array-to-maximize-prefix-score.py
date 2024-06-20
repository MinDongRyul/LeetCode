class Solution(object):
    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        temp, r = 0, 0
        nums = sorted(nums, reverse=True)
        
        for idx, num in enumerate(nums):
            nums[idx] = num + temp
            temp = nums[idx]
            
            if temp > 0:
                r += 1
            
        return r