class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0
        
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1

        # for idx in range(len(nums)):
        #     k = nums[idx]
        #     for idx_2 in range(idx+1, len(nums)):
        #         if nums[idx_2] != 0 and k == 0:
        #             nums[idx_2], nums[idx] = k, nums[idx_2]
        #             idx += 1