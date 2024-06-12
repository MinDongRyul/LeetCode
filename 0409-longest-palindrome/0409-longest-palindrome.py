from collections import Counter, defaultdict

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # use Counter
        # temp = Counter(s)
        
        # use defaultdict
        temp = defaultdict(int)
        for value in s:
            temp[value] += 1

        return min(sum((count[1] - (count[1] % 2) for count in temp.items())) + 1, len(s))