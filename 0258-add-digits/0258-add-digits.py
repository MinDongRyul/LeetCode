# def totalReturn(num):
#     temp = [int(val) for val in str(num)]
#     total = sum(temp)
#     return total

def totalReturn2(num):
    temp = [int(val) for val in str(num)]
    total = sum(temp)
    if total >= 10:
        return totalReturn2(total)
    return total

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        total = totalReturn2(num)
        # while total >= 10:
        #     total = totalReturn(num)
        #     num = total
        return total