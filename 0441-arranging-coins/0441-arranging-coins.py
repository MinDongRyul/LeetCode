class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        while True:
            i += 1
            n = n - i
            if n < 0:
                return i-1
            elif n == 0:
                return i