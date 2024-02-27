class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        rst = []
        while len(str(n)) >= 1:
            temp = [int(val) ** 2 for val in str(n)]

            if sum(temp) == 1:
                return True
            
            n = sum(temp)
            
            if n in rst:
                return False
            
            rst.append(n)