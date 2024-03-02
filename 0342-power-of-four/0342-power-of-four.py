import math

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if n == 1:
        #     return True
        # elif n != 0:
        #     val = math.log(abs(n), 4)
        #     if 4 ** int(val) == n : return True

        if n > 0 and math.log(n,4).is_integer() : return True