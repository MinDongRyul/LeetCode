class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_cycle = len(nums)

        if len_cycle == 0: return nums[0]

        for _ in range(len_cycle-1):
            nums = [(nums[i-1] + nums[i]) % 10 for i in range(1, len(nums))]
        return nums[0]