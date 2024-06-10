class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 내 풀이
        # while len(str(num)) > 1:
        #     num = sum(map(int, str(num)))
        # return num

        # greedy        
        if(num == 0):
            return 0
        return ((num-1)%9)+1