class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_set = set()
        for c in s:
            # s_set에 있으면 c는 이미 두번째 문자
            if c in s_set:
                return c
            # s_set에 없으면 c는 최초 문자
            s_set.add(c)