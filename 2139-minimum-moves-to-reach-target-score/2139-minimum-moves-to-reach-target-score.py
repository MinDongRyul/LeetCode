class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        cnt = 0
        while maxDoubles > 0 and target > 1: 
            if target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            cnt += 1
                
        return cnt + target - 1