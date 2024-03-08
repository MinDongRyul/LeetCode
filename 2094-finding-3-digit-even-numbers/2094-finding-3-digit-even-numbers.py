from itertools import permutations
import collections

class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # r = []
        # three_lst = list(permutations(digits, 3))
        # r = sorted([int(str(nums[0])+str(nums[1])+str(nums[2])) for nums in three_lst if nums[2] % 2 == 0 and nums[0] != 0])
        # return r
        
        res = []
        # Counter({0: 1, 1: 1, 2: 1, 3: 1})
        dp = collections.Counter(digits)
        for i in range(100,999): 
            if i%2 == 0:
                s = str(i)
                ans = []
                for j in s: 
                    ans.append(int(j)) 
                subdp = collections.Counter(ans)
                flag = True
                for k in subdp: 
                    if subdp[k] > dp[k]: 
                        flag = False
                        
                # 각 숫자의 value 값이 같으면 해당 숫자를 만들 수 있다는 것
                if flag:
                    res.append(i)

        return res