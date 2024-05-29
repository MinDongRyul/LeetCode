class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # while 문 사용해서 풀기
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            matrix = list(zip(*matrix))[::-1]
        return res

        # 재귀로 풀기
        # return matrix and list(matrix.pop(0)) + self.spiralOrder(list(zip(*matrix))[::-1])