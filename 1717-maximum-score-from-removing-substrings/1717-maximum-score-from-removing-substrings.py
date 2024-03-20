def check_str(check, s, x, y, r):
    stack = [s[0]]
    for str_ in s[1:]:
        if stack and stack[-1] + str_ == check:
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

        # 좋은 답
        # a, b = 'ab', 'ba'
        # if y > x: 
        #     x, y = y, x
        #     a, b = 'ba', 'ab'
        # stack1 = []
        # ans = 0
        # for le in s:
        #     if stack1 and stack1[-1] == a[0] and le == a[1]: 
        #         stack1.pop()
        #         ans += x
        #     else: stack1.append(le)
        # stack2 = []
        # for le in stack1:
        #     if stack2 and stack2[-1] == b[0] and le == b[1]: 
        #         stack2.pop()
        #         ans += y
        #     else: stack2.append(le)
        # return ans