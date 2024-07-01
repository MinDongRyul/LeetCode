from collections import deque

class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        queue = deque(i for i in range(1, n+1))
        t = 1
        while len(queue) > 1:
            if t == k:
                queue.popleft()
                t = 1
            else:
                queue.append(queue.popleft())
                t += 1
            
        return queue[0]