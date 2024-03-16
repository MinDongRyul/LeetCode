class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sorted_nums = sorted(nums)
        for _ in range(len(nums)):
            num = nums.pop(0)
            nums.append(num)
            if nums == sorted_nums:
                return True