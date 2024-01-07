class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(x)
        rev_x = str_x[::-1]

        if x >= 0: # 양수인 경우
            temp = rev_x
            rst = int(temp)
        else: # 음수인 경우
            minus = str_x[0] # '-' 부호
            temp = rev_x[:-1]
            rst = int(minus + temp)

        if -2**31 <= rst <= 2**31 -1:
            return rst
        else:
            return 0