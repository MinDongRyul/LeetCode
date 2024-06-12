from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = Counter(s)
        return min(sum((count[1] - (count[1] % 2) for count in temp.items())) + 1, len(s))