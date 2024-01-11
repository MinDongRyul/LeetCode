class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        x = columnNumber
        temp = x

        cnt = 0
        while x > 26:
            x //= 26
            cnt += 1

        rst = []
        for idx in range(cnt, -1, -1):
            rst.append(temp // (26 ** idx))
            temp %= (26 ** idx)
            
        for idx in range(len(rst)-1):
            if rst[idx+1] == 0:
                rst[idx], rst[idx+1] = rst[idx]-1, 26

        for idx in range(len(rst)-1):
            if rst[idx] == 1 and rst[idx+1] == 0:
                rst[idx+1] = 26
                rst[idx] = -1
            elif rst[idx+1] == 0:
                rst[idx+1] = 26
                rst[idx] -= 1
                
        return ''.join([chr(num+64) for num in rst if num > 0])