class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        res = []
        self.dfs(candidates, target, [], res)
        return res
        
    def dfs(self, candidates, target, path, res):
        # target이 0보다 작으면 path가 더 큼
        if target < 0:
            return
        # target이 0이면 path가 조건에 만족
        if target == 0:
            res.append(path)
            return
        for i in range(len(candidates)):
            self.dfs(candidates[i:], target - candidates[i], path + [candidates[i]], res)