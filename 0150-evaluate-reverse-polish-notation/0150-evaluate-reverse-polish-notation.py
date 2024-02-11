import math

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []
        for token in tokens:
            if token not in ["+", "-", "/", "*"]: # digit
                stack.append(int(token))
            else: # not digit
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "+":
                    total = num2 + num1
                elif token == "-":
                    total = num2 - num1
                elif token == "*":
                    total = num2 * num1
                elif num2 // num1 >= 0: 
                    total = num2 // num1
                elif num2 // num1 < 0: 
                    # 5/-2 -> -3, 4/-2 -> -2
                    total = abs(num2) / abs(num1) * -1
                stack.append(total)
        return stack[0]