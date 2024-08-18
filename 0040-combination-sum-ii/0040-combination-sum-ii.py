class Solution(object):
    # def combinationSum2(self, candidates, target):
    #     """
    #     :type candidates: List[int]
    #     :type target: int
    #     :rtype: List[List[int]]
    #     """
    #     candidates = sorted(candidates)
    #     res = []
        
    #     self.dfs(candidates, target, [], res)
    #     return res
    
    # def dfs(self, candidates, target, path, res):
    #     if target < 0:
    #         return
    #     if target == 0 and path not in res:
    #         res.append(path)
    #         return
        
    #     for idx in range(len(candidates)):
    #         self.dfs(candidates[idx+1:], target-candidates[idx], path + [candidates[idx]], res)

    def combinationSum2(self, candidates, target):
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
        if target < 0:
            return
        if target == 0:
            res.append(path)
        
        for idx in range(len(candidates)):
            
            if idx > 0 and candidates[idx] == candidates[idx-1]:
                continue
                
            if candidates[idx]> target:
                break
            
            self.dfs(candidates[idx+1:], target-candidates[idx], path + [candidates[idx]], res)