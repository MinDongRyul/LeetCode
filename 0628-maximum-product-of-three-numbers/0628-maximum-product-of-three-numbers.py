class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)        
        # len_nums = len(nums)
        max_val_1 = nums[0] * nums[1] * nums[-1]
        # max_val_2 = nums[len_nums-1] * nums[len_nums-2] * nums[len_nums-3]
        max_val_2 = nums[-1] * nums[-2] * nums[-3]
        
        return max(max_val_1, max_val_2)