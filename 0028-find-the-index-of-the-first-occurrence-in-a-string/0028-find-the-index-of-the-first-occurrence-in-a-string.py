class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            # 안에 들어 있는 경우
            for idx in range(0, len(haystack)-len(needle)+1):
                if haystack[idx:idx+len(needle)] == needle:
                    return idx
        else:
            return -1