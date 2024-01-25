class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for idx, num in enumerate(nums):
            if num >= target:
                return idx
        return len(nums)