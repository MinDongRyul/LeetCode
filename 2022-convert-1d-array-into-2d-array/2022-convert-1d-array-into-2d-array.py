class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if len(original) == m * n:
            return [original[row*n:(row+1)*n] for row in range(m)]
        return []