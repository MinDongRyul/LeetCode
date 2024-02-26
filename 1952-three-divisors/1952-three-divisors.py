class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        total = 2
        for idx in range(2, n//2+1):
            if n % idx == 0:
                total += 1    
        if total == 3: return True