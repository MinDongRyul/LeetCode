def check_str(check, s, x, y, r):
    stack = [s[0]]
    for str_ in s[1:]:
        if len(stack) >= 1 and stack[-1] + str_ == check:
            stack.pop()
            r += x
        else:
            stack.append(str_)
    return ''.join(stack), r

class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        
        r = 0
        
        # max point부터 처리
        if x > y: # x 가 max point인 경우
            while 'ab' in s:
                s, r = check_str('ab', s, x, y, r)
        else: # y가 max point 인 경우
            while 'ba' in s:
                s, r = check_str('ba', s, y, x, r)
                    
        if x < y: # 이미 위에서 x > y 일때 max 인 경우를 함
            while 'ab' in s:
                s, r = check_str('ab', s, x, y, r)
        else:
            while 'ba' in s:
                s, r = check_str('ba', s, y, x, r)
        
        return r