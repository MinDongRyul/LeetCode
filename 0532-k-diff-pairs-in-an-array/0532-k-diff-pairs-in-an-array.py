class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        
        ex)
        nums = [3,1,4,1,5]
        k = 2
        r = 2
        
        nums = [1,2,3,4,5]
        k = 1
        output = 4
        """
        r = set()
        for i in range(len(nums)):
            val1, val2 = nums[i]+k, nums[i]-k
            if val1 in nums[i+1:]:
                r.add(tuple(sorted([nums[i], val1])))
            if val2 in nums[i+1:]:
                r.add(tuple(sorted([nums[i], val2])))
        return len(r)