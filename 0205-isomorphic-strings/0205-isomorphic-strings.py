class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_ = [s.index(val) for val in s]
        t_ = [t.index(val) for val in t]
        if s_ == t_: return True