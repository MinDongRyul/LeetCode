class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(mat) * len(mat[0]) == r * c:
            output = []
            for mat_ in mat:
                output += mat_
            # return [output[idx*c:(idx+1)*c] for idx in range(0, r)]
            return [output[idx:idx+c] for idx in range(0, len(output), c)]
        else:
            return mat