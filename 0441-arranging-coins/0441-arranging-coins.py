from math import sqrt

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 메모리 비효율적
        # i = 0
        # while True:
        #     i += 1
        #     n = n - i
        #     if n < 0:
        #         return i-1
        #     elif n == 0:
        #         return i

        return int((sqrt(8 * n + 1) - 1) / 2)