class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # ex
        # k = 32
        # n = 3
        k -= n
        alpha = '_bcdefghijklmnopqrstuvwxy_'
        # ans = 'z' * (32//25)
        # ans 'z'
        ans = 'z' * (k // 25)
        if k % 25:
            # ans = alpha[4] + 'z'
            # ans = 'ez'
            ans = alpha[k % 25] + ans
        
        # 'a' * (3 - len(ans)) + 'ez'
        # 'a' * (3 - 2) + 'ez'
        # 'aez'
        return 'a' * (n - len(ans)) + ans