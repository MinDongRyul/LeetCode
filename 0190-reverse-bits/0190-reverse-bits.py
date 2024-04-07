class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # int -> bit
        n = format(n, 'b')
        # bit -> 32bit
        n = n.zfill(32)
        return int(n[::-1], 2) # 32bit -> int