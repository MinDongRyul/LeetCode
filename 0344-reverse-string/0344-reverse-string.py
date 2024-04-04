class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for idx in range(len(s)//2):
            k = s[len(s)-idx-1]
            s[len(s)-idx-1] = s[idx]
            s[idx] = k