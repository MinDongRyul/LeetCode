import collections

class Solution:
    def longestPalindrome(self, s):
        return min(sum(count - (count % 2) for count in collections.Counter(s).values()) + 1, len(s))