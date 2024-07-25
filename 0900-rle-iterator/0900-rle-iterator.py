class RLEIterator(object):

    def __init__(self, encoding):
        # 뒤집는건 뒤집고 pop을 할 경우 기존 맨처음에 있었던 수를 기준으로 잡을 수 있음
        self.rle = encoding[::-1]

    def next(self, n):
        acc = 0
        while acc < n:
            # 아무 값도 없으면 return -1 
            if not self.rle:
                return -1
            times, num = self.rle.pop(), self.rle.pop()
            acc += times
        if acc > n:
            self.rle.append(num)
            self.rle.append(acc - n)
        return num

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)