class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        len_nums = len(nums)
        r = set((nums[idx] + nums[len_nums-idx-1])/2 for idx in range(0, len_nums//2))
            
        return 4