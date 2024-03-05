class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # ret = []
        # nums.sort()
        # for idx, val in enumerate(nums):
        #     if val == target:
        #         ret.append(idx)
        # return ret

        # target 보다 큰 숫자는 무시하며 작은 숫자는 lt_count 갯수에 추가
        # target와 같은 숫자는 eq_count 갯수에 추가
        lt_count = eq_count = 0
        for n in nums:
            if n < target:
                lt_count += 1
            elif n == target:
                eq_count += 1
            
        return list(range(lt_count, lt_count+eq_count))