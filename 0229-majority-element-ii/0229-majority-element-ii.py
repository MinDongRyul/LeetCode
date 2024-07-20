from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        times = len(nums) / 3
        temp = Counter(nums)
        cnt = []
        for key, value in temp.items():
            if value > times:
                cnt.append(key)
        return cnt