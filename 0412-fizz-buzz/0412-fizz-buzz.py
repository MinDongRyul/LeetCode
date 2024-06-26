class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        temp = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                temp.append('FizzBuzz')
            elif i % 5 == 0:
                temp.append('Buzz')
            elif i % 3 == 0:
                temp.append('Fizz')
            else:
                temp.append(str(i))
        return temp
        
