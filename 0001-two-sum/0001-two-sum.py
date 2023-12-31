class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rst = []
        for idx in range(len(nums)):
            a = nums[idx]
            for idx_2 in range(idx+1, len(nums)):
                b = nums[idx_2]
                if a + b == target:
                    rst.append(idx)
                    rst.append(idx_2)
        return rst
        