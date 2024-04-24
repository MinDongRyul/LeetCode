from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        cs = sorted(Counter(s).items(), key=lambda x : x[1], reverse=True)
        r = ''
        for val in cs:
            r += val[0] * val[1]
        return r