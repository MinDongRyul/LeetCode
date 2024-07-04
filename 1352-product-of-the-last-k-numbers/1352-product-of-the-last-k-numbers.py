class ProductOfNumbers(object):

    def __init__(self):
        self.get_list = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        # num을 무작정 넣는게 아니라 넣을때부터 접두사의 곱의 값으로 넣음
        # 단 0이면 초기화
        if num == 0:
            self.get_list = [1]
        else:
            self.get_list.append(self.get_list[-1] * num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """

        if k >= len(self.get_list): return 0
        # get_list[-1] : 현재까지 모든 값의 곱
        # get_list[-k-1] : 만약 k가 2면 [1, 2, 3, 4]기준 3 * 4임
        # 다만 get_list 는 모든 값의 곲을 가지고 있기에 
        # get_list[-1] : 1*2*3*4 / get_list[-3] : 1*2 를 나눠줌으로써 3*4의 값을 가져올 수 있음 
        return self.get_list[-1] / self.get_list[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)