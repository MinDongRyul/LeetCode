class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1

        r = sum([item[0] for item in nums_dict.items() if item[1] == 1])        
        # r = sum([key for key in nums_dict.keys() if nums_dict[key] == 1])
        return r