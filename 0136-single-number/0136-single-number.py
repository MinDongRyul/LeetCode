class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}
        for num in nums:
            if str(num) not in num_dict.keys():
                num_dict[str(num)] = 1
            else:
                num_dict[str(num)] += 1
        min_nums = min(num_dict, key=lambda k: num_dict[k])
        return int(min_nums)
        