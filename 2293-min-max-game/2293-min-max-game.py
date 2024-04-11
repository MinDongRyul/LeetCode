class Solution(object):
    def minMaxGame(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) > 1:
            len_nums = len(nums)
            for idx in range(0, len_nums, 2):
                if idx % 4 == 0:
                    nums.append(min(nums[idx], nums[idx+1]))
                else:
                    nums.append(max(nums[idx], nums[idx+1]))            
            nums = nums[-(len_nums//2):]
        return nums[0]