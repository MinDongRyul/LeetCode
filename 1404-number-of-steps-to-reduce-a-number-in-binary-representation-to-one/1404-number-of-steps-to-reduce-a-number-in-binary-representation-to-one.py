class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        int_s = int(s, 2)
        cnt = 0
        while int_s > 1:
            if int_s % 2 == 0:
                int_s = int_s >> 1
            else:
                int_s += 1
            cnt += 1

        return cnt