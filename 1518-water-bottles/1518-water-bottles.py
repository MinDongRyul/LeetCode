class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        ret = numBottles
        while numBottles >= numExchange:
            temp = numBottles % numExchange
            numBottles //= numExchange
            ret += numBottles
            numBottles += temp 
        return ret