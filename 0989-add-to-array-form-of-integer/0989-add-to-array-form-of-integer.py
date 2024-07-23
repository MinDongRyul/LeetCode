class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        return [int(val) for val in str(int(''.join(list(map(str, num)))) + k)]