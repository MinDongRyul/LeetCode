from queue import PriorityQueue

class Solution(object):
    def splitNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        # nums = [val for val in str(num)]
        # nums.sort()
        # nums_1 = [val for idx, val in enumerate(nums) if idx % 2 != 0]
        # nums_2 = [val for idx, val in enumerate(nums) if idx % 2 == 0]
        # ret = int(''.join(nums_1)) + int(''.join(nums_2))
        # return ret

        a = [int(x) for x in str(num)]
        pq = PriorityQueue()
        num1 = ""
        num2 = ""
        for i in a:
            pq.put(i)
        while not pq.empty():
            # pq.get() 은 Priority Queue 에서 최솟값만 배출 해줌
            num1 += str(pq.get())
            if not pq.empty():
                num2 += str(pq.get())
        if num2:
            return int(num1) + int(num2)
        else:
            return int(num1)