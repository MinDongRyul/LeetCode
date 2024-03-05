class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ret = []
        nums.sort()
        for idx, val in enumerate(nums):
            if val == target:
                ret.append(idx)
        return ret