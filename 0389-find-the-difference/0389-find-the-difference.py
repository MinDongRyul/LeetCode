class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = sorted(s)
        t = sorted(t)
        for idx, val in enumerate(s):
            if val != t[idx]:
                return t[idx]
        return t[-1]