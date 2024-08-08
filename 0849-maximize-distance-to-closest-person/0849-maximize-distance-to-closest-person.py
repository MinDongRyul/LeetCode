class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        temp = []
        temp.append(seats.index(1))
        temp.append(seats[::-1].index(1))
        
        last_idx = len(seats) - seats[::-1].index(1)
        
        cnt = 0
        for seat in seats[seats.index(1):last_idx]:
            if seat == 1:
                cnt +=1
                temp.append(cnt//2)
                cnt = 0
            else:
                cnt += 1
        
        return max(temp)