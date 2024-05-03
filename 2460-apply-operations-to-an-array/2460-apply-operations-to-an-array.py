class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for idx in range(len(nums)-1):
            if nums[idx] == nums[idx+1]:
                nums[idx] *= 2
                nums[idx+1] = 0
        
        r = [0] * len(nums)
        r_i = 0
        for num in nums:
            if num != 0:
                r[r_i] = num
                r_i += 1
                
        return r