class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        temp = {}
        for idx, num in enumerate(nums):
            if num in temp and abs(idx - temp[num]) <= k:
                return True
            else:
                temp[num] = idx
        return False

        # fail code
        # for idx, num in enumerate(nums):
        #     for idx2, num2 in enumerate(nums):
        #        if idx != idx2 and nums[idx] == nums[idx2] and abs(idx - idx2) <= k:
        #            return True
        # return False