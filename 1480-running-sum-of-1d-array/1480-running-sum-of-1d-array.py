class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # temp = 0
        # for idx, num in enumerate(nums):
        #     nums[idx] = temp + num
        #     temp = nums[idx]
        # return nums

        for idx in range(1, len(nums)):
            nums[idx] += nums[idx-1]
        return nums