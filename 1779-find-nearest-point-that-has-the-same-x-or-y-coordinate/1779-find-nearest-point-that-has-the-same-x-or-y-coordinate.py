class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        min_ = 20000
        for point in points:
            if x == point[0] or y == point[1]:
                if min_ > abs(x-point[0]) + abs(y-point[1]):
                    min_ = abs(x-point[0]) + abs(y-point[1])
                    r = points.index(point)
        if min_ == 20000: return -1
        return r