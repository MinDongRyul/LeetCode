from collections import Counter

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_ = Counter(nums)
        r = [num for num, cn in nums_.items() if cn == 2]
        return r 