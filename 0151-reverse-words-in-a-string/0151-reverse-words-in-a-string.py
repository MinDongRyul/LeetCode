class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = s.strip().split()
        return ' '.join(lst[::-1])