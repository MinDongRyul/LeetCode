class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        remove = []
        for idx, val in enumerate(nums):
            if idx == nums.index(val):
                ret += 1
            else:
                remove.append(idx)
        
        remove.sort(reverse=True)
                
        for remove_num in remove:
            nums.pop(remove_num)
                
        return ret