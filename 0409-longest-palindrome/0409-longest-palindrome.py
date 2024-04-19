import collections

class Solution:
    def longestPalindrome(self, s):
        # return min(sum(count - (count % 2) for count in collections.Counter(s).values()) + 1, len(s))temp = {}
        temp = {}
        for val in s:
            if val not in temp:
                temp[val] = 1
            else:
                temp[val] += 1
        return min(sum((count[1] - (count[1] % 2) for count in temp.items())) + 1, len(s))