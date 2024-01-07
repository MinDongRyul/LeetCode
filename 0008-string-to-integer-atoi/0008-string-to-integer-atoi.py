class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        rst = []
        s = s.strip()
        temp = [str(str_) for str_ in s]

        for temp_ in temp:
            if str.isdigit(temp_) or temp_ in ['+', '-']:
                if temp_ in ['+', '-'] and len(rst) == 0:
                    rst.append(temp_)
                elif temp_ in ['+', '-'] and len(rst) ==1 and rst[0] in ['+', '-']:
                    rst = ['0']
                    break
                elif temp_ in ['+', '-'] and rst[0] in ['+', '-']:
                    break
                elif temp_ in ['+', '-'] and len(rst) > 0:
                    break
                else:
                    rst.append(temp_)
            elif len(rst) == 0 and not str.isdigit(temp_):
                rst = ['0']
                break
            elif len(rst) != 0 and not str.isdigit(temp_):
                break

        if len(temp) == 0:
            total = 0
        elif len(rst) == 1 and rst[0] in ['+', '-', '.']:
            total = 0
        else:
            total = (int(''.join(rst)))

        if total <= -2 ** 31:
            return (-2 ** 31)
        elif total >= 2**31 -1:
            return (2 ** 31 - 1)
        else:
            return (total)