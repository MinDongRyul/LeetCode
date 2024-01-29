class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 1:
            return True
        elif n <= 0:
            return False
        else:
            i = 2
            while i <= n:
                if n % i == 0:
                    n = n / i
                else:
                    i = i + 1
                if i >= 6:
                    return False
        return True
        