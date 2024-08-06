class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        cnt = 0
        for st in s:
            if st == '(':
                stack.append(st)
            else:
                if stack:
                    stack.pop()
                else:
                    cnt += 1
        return len(stack) + cnt