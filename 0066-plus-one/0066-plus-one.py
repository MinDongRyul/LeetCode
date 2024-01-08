class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [str(num) for num in digits]
        digits = ''.join(digits)
        temp = (int(digits)+1)
        temp = str(temp)
        return [int(num) for num in temp]