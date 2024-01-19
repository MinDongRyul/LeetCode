class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 안에 들어 있는 경우
        for idx in range(len(haystack)-len(needle)+1):
            if haystack[idx:idx+len(needle)] == needle:
                return idx
        return -1