class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = nums[:1]
        right = nums[1:]
        while max(left) > min(right):
            temp = right.index(min(right)) + 1
            left = left + right[:temp]
            right = right[temp:]
        return len(left)