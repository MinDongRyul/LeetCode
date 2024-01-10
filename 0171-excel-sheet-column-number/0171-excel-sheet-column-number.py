class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        
        temp = [(ord(col)-64) * (26 ** idx) for idx, col in enumerate(columnTitle[::-1])]
        return sum(temp)
        