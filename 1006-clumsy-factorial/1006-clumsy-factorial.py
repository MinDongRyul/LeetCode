from collections import deque

class Solution(object):
    def clumsy(self, n):
        """
        :type n: int
        :rtype: int
        """
        con = deque(['*', '/', '+', '-'])
        stack = []
        for num in range(n, 0, -1):
            stack.append(num)
            stack.append(con[0])
            con.rotate(-1)
        stack = stack[:-1]
        temp = [stack.pop(0)]
        
        while stack:
            con = stack.pop(0)
            num_2 = stack.pop(0)
            
            if con == '*':
                num_1 = temp.pop(-1)
                temp.append(num_1 * num_2)
            elif con == '/':
                num_1 = temp.pop(-1)
                temp.append(num_1 // num_2)
            else:
                temp.append(con)
                temp.append(num_2)
                
        ret = [temp.pop(0)]        
        while '+' in temp or '-' in temp:
                        
            con = temp.pop(0)
            num_2 = temp.pop(0)
            
            if con == '+':
                num_1 = ret.pop(-1)
                ret.append(num_1 + num_2)
            elif con == '-':
                num_1 = ret.pop(-1)
                ret.append(num_1 - num_2)
        
        return ret[0]