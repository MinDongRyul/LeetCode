class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 내 풀이
        # num1 = sum(nums) # list sum
        # num2 = sum([sum(map(int, str(num))) for num in nums])
        # return abs(num1 - num2)

        res = 0
        for num in nums:
            if num >= 10:
                res += num
                while num > 0:
                    res -= num%10
                    num /= 10
        return res  