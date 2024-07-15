class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(n + 1):
            # Convert number to binary and count the number of 1's
            count_ones = bin(i).count('1')
            ans.append(count_ones)
        return ans