class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_lst = [(2 ** idx) * int(num) for idx, num in enumerate(a[::-1])]
        b_lst = [(2 ** idx) * int(num) for idx, num in enumerate(b[::-1])]
        
        total = sum(a_lst + b_lst)
        temp = []
        
        if total == 0:
            return '0'

        while total > 0:
            
            temp.append(str(total % 2))
            
            total = total // 2
        
        rst = ''.join(temp[::-1])
        
        
        return rst