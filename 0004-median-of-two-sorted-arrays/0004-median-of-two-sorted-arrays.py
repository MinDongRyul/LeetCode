class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = nums1 + nums2
        nums3.sort()
        len_nums = len(nums3)
        median_num = len_nums / 2
        # 짝수
        if len_nums % 2 == 0:
            return (float(nums3[median_num-1])+float(nums3[median_num]))/2.0
        else: # 홀수
            return nums3[median_num]
