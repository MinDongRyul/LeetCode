class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # stack = []
        # temp = []
        # r = []
        
        # if not nums:
        #     return []
        
        # for num in nums:
        #     if not stack or abs(stack[-1] - num) == 1:
        #         stack.append(num)
        #     else:
        #         temp.append(stack)
        #         stack = [num]
        # temp.append(stack)
        
        # r = [str(val[0]) if val[0] == val[-1] else str(val[0]) + "->" + str(val[-1]) for val in temp]
        
        # return r

        # 좋은 정답 표본
        ranges = [] # [start, end] or [x, y]
        for n in nums:
            # ex
            # n : 0 -> ranges.append([0, 0])
            # n : 1 -> range[-1] : [0, 0], range[-1][1] : 0
            #       -> range[-1][1] == n - 1 -> range[-1][1] == n 
            if ranges and ranges[-1][1] == n-1:
                ranges[-1][1] = n
            else:
                ranges.append([n, n])
        return [str(x) + '->' + str(y) if x != y else str(x) for x, y in ranges]

