class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_cycle = len(nums)
        for _ in range(len_cycle-1):
            temp = []
            for i in range(1, len(nums)):
                temp.append((nums[i-1] + nums[i]) % 10)
            nums = temp 
        return nums[0]