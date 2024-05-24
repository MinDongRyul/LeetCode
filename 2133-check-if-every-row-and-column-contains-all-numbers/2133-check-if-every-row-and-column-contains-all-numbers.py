from collections import defaultdict

class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row, col = defaultdict(int), defaultdict(int)
        
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                row[matrix[x][y]] += 1 # row -> column
                col[matrix[y][x]] += 1 # column -> row

            for row_, col_ in zip(row, col):
                if row[row_] > x+1 or col[col_] > x+1:
                    return False
                
        return True