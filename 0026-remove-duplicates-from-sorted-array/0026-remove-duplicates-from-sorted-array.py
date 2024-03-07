class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # temp = set()
        # for val in nums:
        #     temp.add(nums.index(val))
        # nums[:] = [nums[val] for val in temp]
        # return len(temp)

        # ret = 0
        # remove = []
        # for idx, val in enumerate(nums):
        #     if idx == nums.index(val):
        #         ret += 1
        #     else:
        #         remove.append(idx)
        
        # remove.sort(reverse=True)
                
        # for remove_num in remove:
        #     nums.pop(remove_num)
                
        # return ret

        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j