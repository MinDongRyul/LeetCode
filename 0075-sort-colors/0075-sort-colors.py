class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # insert sorting
        for val in range(1, len(nums)):
            key = nums[val]
            i = val - 1
            while i >= 0 and nums[i] > key:
                nums[i + 1] = nums[i]
                i = i - 1
            nums[i+1] = key