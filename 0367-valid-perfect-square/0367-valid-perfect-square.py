class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        lo = 2
        hi = num // 2
        while lo <= hi:
            mid = lo + (hi - lo) //2
            print(mid)
            if mid * mid == num:
                return True
            if mid * mid > num:
                hi = mid - 1
            else:
                lo = mid + 1
        return False

        # fail code
        # if num == 1:
        #     return True
        # else:
        #     for idx in range(1, num+1):
        #         if num%idx == 0 and idx == num//idx:
        #             return True