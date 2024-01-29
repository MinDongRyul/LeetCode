class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n >= 1:
            while n % 3 == 0:
                n //= 3
            return n == 1
        # if n <= 0:
        #     return False
        # elif n == 1:
        #     return True
        # else:
        #     while True:
        #         if n == 1:
        #             return True
        #         elif n % 3 != 0:
        #             return False
        #         else:
        #             n /= 3