class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        maxLen = max([min(rectangle) for rectangle in rectangles])
        r = 0
        for rectangle in rectangles:
            if min(rectangle) == maxLen:
                r += 1
        return r

        # maxsq=[]
        # for i in rectangles:
        #     maxsq.append(min(i))
        # print maxsq
        # return maxsq.count(max(maxsq))