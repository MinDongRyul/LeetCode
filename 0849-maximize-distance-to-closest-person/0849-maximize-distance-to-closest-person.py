class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        last_one_idx = seats[::-1].index(1)
        first_one_idx = seats.index(1)
        temp = [first_one_idx, last_one_idx]
        last_idx = len(seats) - last_one_idx
        cnt = 0
        for seat in seats[first_one_idx:last_idx]:
            cnt +=1
            if seat == 1:
                temp.append(cnt//2)
                cnt = 0
        return max(temp)