class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        mp="0123456789abcdef"
        ans=""
        for _ in range(8): # 2^32 -> 16^8
            ans=mp[num%16]+ans
            # -1%16 -> 15
            num=num//16
            # -1//16 -> -1
        return ans.lstrip('0') # 0000001a -> 1a 