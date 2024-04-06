class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        stack = []
        temp = []
        r = []
        
        if not nums:
            return []
        
        for num in nums:
            if not stack or abs(stack[-1] - num) == 1:
                stack.append(num)
            else:
                temp.append(stack)
                stack = [num]
        temp.append(stack)
        
        for val in temp:
            if val[0] == val[-1]:
                r.append(str(val[0]))
            else:
                r.append(str(val[0]) + "->" + str(val[-1]))
        
        return r