class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, x in enumerate(nums):
            if (target - x) in nums[idx+1:]:
                return [idx, nums.index(target-x, idx+1)]