class Solution:
    def isValid(self, s: str) -> bool:
        lst = [str_ for str_ in s]
        stack = [s[0]]

        for s in lst[1:]:
            if len(stack) != 0 and stack[-1]+s in ['()', '{}', '[]']:
                stack.pop(-1)
            else:
                stack.append(s)
            
        if len(stack) == 0:
            return True
        else:
            return False