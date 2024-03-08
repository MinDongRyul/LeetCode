class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        result = [0, 0]
        i = 0
        while n:
            result[i] += n & 1
            n >>= 1
            i ^= 1

        return result
        
#         temp = ''
#         even, odd = 0, 0
#         while n > 0:
#             temp += str(n % 2)
#             n //= 2
        
#         for idx, val in enumerate(temp):
#             if idx % 2 == 0 and val == '1':
#                 even += 1
#             elif val == '1':
#                 odd += 1
                
#         return [even, odd]