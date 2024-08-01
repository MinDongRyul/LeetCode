class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxi = max(A)
        mini = min(A)
        return max(0, maxi-K-mini-K)