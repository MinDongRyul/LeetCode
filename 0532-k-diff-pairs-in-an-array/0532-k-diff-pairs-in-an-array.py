from collections import Counter

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # r = set()
        # for i in range(len(nums)):
        #     val1, val2 = nums[i]+k, nums[i]-k
        #     if val1 in nums[i+1:]:
        #         r.add((nums[i], val1))
        #     if val2 in nums[i+1:]:
        #         r.add((val2, nums[i]))
        # return len(r)
        freq_count = Counter(nums)
        k_pair_count = 0

        for key, value in freq_count.items():
            if k == 0:
                if value > 1:
                    k_pair_count += 1
            else:
                if (key + k) in freq_count:
                    k_pair_count += 1
        
        return k_pair_count