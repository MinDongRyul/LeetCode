class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        
        # 결국에는 최소 범위가 최대 값을 가지는 갯수가 되는 구조
        min_x = min(op[0] for op in ops)
        min_y = min(op[1] for op in ops)

        return min_x * min_y