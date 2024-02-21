class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lst_len = len(nums)
        for i in range(lst_len+1):
            if i not in nums:
                return i