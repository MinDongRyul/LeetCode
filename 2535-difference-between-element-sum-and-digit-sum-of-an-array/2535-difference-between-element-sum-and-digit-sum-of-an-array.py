class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num1 = sum(nums) # list sum
        num2 = sum([sum(map(int, str(num))) for num in nums])
        return abs(num1 - num2)