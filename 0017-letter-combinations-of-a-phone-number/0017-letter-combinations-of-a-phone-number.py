class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        # 비어있으면 return
        if len(digits) == 0:
            return res
            
        self.dfs(digits, 0, dic, '', res)
        return res
    
    def dfs(self, nums, index, dic, path, res):
        # index 가 digits의 길이보다 커지면 pass
        if index >=len(nums):
            res.append(path)
            return
        
        # dic[nums[index]] -> dic[2]
        # string1 = dic[2] (abc)
        string1 = dic[nums[index]]
        for i in string1:
            # i = a, b, c
            # index = 1
            # dfs를 통해 재귀를 돌음
            self.dfs(nums, index+1, dic, path + i, res)