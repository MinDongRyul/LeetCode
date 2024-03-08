class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                r += 1
        return r