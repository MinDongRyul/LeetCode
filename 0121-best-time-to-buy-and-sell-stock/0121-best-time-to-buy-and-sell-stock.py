class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_ = 0
        min_ = prices[0]
        for val in prices[1:]:
            if val < min_:
                min_ = val
            else:
                max_ = max(max_, val - min_)
        return max_