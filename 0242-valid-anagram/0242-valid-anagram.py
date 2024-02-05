class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_ = [str1 for str1 in s]
        t_ = [str1 for str1 in t]
        s_.sort()
        t_.sort()
        if s_ == t_:
            return True
            