def totalReturn(num):
    temp = [int(val) for val in str(num)]
    total = sum(temp)
    return total

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        total = totalReturn(num)
        while total >= 10:
            total = totalReturn(num)
            num = total
        return total