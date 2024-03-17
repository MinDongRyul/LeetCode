class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        min_01 = '01' * (len_s // 2 + 1)
        min_10 = '10' * (len_s // 2 + 1)
        total_01, total_10 = 0, 0
        
        for idx in range(len_s):
            if s[idx] != min_01[idx]:
                total_01 += 1
                
            if s[idx] != min_10[idx]:
                total_10 += 1
                
        return min(total_01, total_10)