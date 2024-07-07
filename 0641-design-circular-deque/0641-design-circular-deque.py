class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k
        self.deque = []

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.deque) >= self.k:
            return False
        else:
            self.deque.insert(0, value)
            return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.deque) >= self.k:
            return False
        else:
            self.deque.append(value)
            return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.deque:
            self.deque.pop(0)
            return True
        else:
            return False

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.deque:
            self.deque.pop()
            return True
        else:
            return False

    def getFront(self):
        """
        :rtype: int
        """
        if self.deque:
            return self.deque[0]
        else:
            return -1

    def getRear(self):
        """
        :rtype: int
        """
        if self.deque:
            return self.deque[-1]
        else:
            return -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.deque:
            return False
        else:
            return True

    def isFull(self):
        """
        :rtype: bool
        """
        if len(self.deque) == self.k:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()