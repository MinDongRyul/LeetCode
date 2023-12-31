class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_2 = str(x)[::-1]
        if str(x) == x_2:
            return True
        else:
            return False