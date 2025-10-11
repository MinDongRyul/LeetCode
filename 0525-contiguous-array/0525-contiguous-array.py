class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        dic = {}
        count, max_length = 0, 0
        dic[0] = -1
        for i in range(len(nums)):
            count += 1 if(nums[i]) else -1
            if count in dic:
                max_length = max(i - dic[count], max_length)
            else:
                dic[count] = i
        return max_length