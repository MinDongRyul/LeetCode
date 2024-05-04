class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        len_nums = len(nums)
        r = set((float(nums[idx]) + nums[-1-idx]) / 2 for idx in range(0, len_nums//2))

        return len(r)