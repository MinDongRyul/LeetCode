from collections import defaultdict, Counter

class Solution(object):
    def largestPalindromic(self, num):
        """
        :type num: str
        :rtype: str
        """
        
        # nums = defaultdict(int)
        # for value in sorted(num, reverse=True):
        #     nums[value] += 1
        
        nums = Counter(num)
        res = ''.join(nums[i] // 2 * i for i in '9876543210').lstrip('0')
        mid = max(nums[i] % 2 * i for i in nums)
        return (res + mid + res[::-1]) or '0'