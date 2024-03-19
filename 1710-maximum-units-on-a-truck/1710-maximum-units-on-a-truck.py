class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        r = 0
        boxTypes.sort(key=lambda x : x[1], reverse=True)
        for box_type in boxTypes:
            if truckSize - box_type[0] >= 0:
                r += box_type[0] * box_type[1]
                truckSize -= box_type[0]
            else:
                r += truckSize * box_type[1]
                break
        return r