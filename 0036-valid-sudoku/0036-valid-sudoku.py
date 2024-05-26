def check_row_col(matrix):
    for row in matrix:
        for idx, row_ in enumerate(row):
            if row_ in row[idx+1:] and row_.isdecimal():
                return False
    return True

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # row, col check
        # 9x9 board check
        # False -> return False
        # if not check_row_col(board) or not check_row_col(list(zip(*board))): return False

        # # 3x3 board check
        # temp_1, temp_2, temp_3 = [], [], []
        # for idx, row in enumerate(board):
        #     temp_1 += row[:3]
        #     temp_2 += row[3:6]
        #     temp_3 += row[6:]
        #     if idx % 3 == 2:
        #         if check_row_col([temp_1]) and check_row_col([temp_2]) and check_row_col([temp_3]):
        #             temp_1, temp_2, temp_3 = [], [], []
        #         else:
        #             return False
        
        # return True
        big = set()
        for i in xrange(0,9):
            for j in xrange(0,9):
                if board[i][j]!='.':
                    cur = board[i][j]
                    if (i,cur) in big or (cur,j) in big or (i/3,j/3,cur) in big:
                        return False
                    big.add((i,cur))
                    big.add((cur,j))
                    big.add((i/3,j/3,cur))
        return True