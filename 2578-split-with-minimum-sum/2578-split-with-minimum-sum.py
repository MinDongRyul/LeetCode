class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = [val for val in str(num)]
        nums.sort()
        nums_1 = [val for idx, val in enumerate(nums) if idx % 2 != 0]
        nums_2 = [val for idx, val in enumerate(nums) if idx % 2 == 0]
        ret = int(''.join(nums_1)) + int(''.join(nums_2))
        return ret