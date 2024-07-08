class FrontMiddleBackQueue(object):

    def __init__(self):
        self.queue = []

    def pushFront(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.queue.insert(0, val)

    def pushMiddle(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.queue.insert(len(self.queue)//2, val)

    def pushBack(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.queue.append(val)

    def popFront(self):
        """
        :rtype: int
        """
        if self.queue:
            return self.queue.pop(0)
        else:
            return -1

    def popMiddle(self):
        """
        :rtype: int
        """
        if len(self.queue) % 2 == 0 and self.queue:
            return self.queue.pop(len(self.queue)//2-1)
        elif len(self.queue) % 2 != 0 and self.queue:
            return self.queue.pop(len(self.queue)//2)
        else:
            return -1

    def popBack(self):
        """
        :rtype: int
        """
        if self.queue:
            return self.queue.pop()
        else:
            return -1
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()