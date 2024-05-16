from collections import defaultdict

class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        ex)
        nums = [4, 1, 3, 3]
        r : 5
        
        nums = [1, 2, 3, 4, 5]
        r : 0
        """
        
        n = len(nums)
        # n : 4 -> 총 fair number : 6
        total = n * (n - 1) // 2
        good = 0        
        mp = defaultdict(int)

        for idx, num in enumerate(nums):
            good += mp[num - idx]
            mp[num-idx] += 1 
            # mp[0]:2 가 되는 순간 0은 2개가 있다는 것 -> 즉 이건 good fair가 한쌍 존재하는다는 것
        return total - good