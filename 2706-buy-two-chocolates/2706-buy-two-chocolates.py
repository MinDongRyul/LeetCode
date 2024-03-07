class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        min_money = prices[0] + prices[1]
        return money - min_money if money >= min_money else money
        # if money >= min_money:
        #     return money - min_money
        # else:
        #     return money