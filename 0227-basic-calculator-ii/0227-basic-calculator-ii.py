class Solution():
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        
        s : "3+2*2"
        r : 7
        
        s : " 3/2 "
        r : 1
        
        s : " 3+5 / 2"
        r : 5
        
        s : "42"
        r : 42
        
        s : "42+5"
        r : 47
        
        """
                
        s = s.replace(' ','')
        temp, temp_str = [], ''
        for val in s:
            if not val.isdigit():
                temp.append(temp_str)
                temp.append(val)
                temp_str = ''
            else:
                temp_str += val
        temp.append(temp_str)
        
        if len(temp) == 1:
            return int(temp[0])
        
        stack, stack2 = [], []
        for idx, val in enumerate(temp):
            if len(stack) != 0 and stack[-1] in ['*', '/']:
                sign = stack.pop()
                num1 = stack.pop()
                if sign == '*':
                    total = str(int(num1) * int(val))
                    stack.append(total)
                else:
                    total = str(int(num1) // int(val))
                    stack.append(total)
            else:
                stack.append(val)

        for idx, val in enumerate(stack):
            if len(stack2) != 0 and stack2[-1] in ['+', '-']:
                sign = stack2.pop()
                num1 = stack2.pop()
                if sign == '+':
                    total = str(int(num1) + int(val))
                    stack2.append(total)
                else:
                    total = str(int(num1) - int(val))
                    stack2.append(total)
            else:
                stack2.append(val)

        return int(stack2[0])