class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[i+m] = nums2[i]
            
        nums1.sort()

        # 1. n의 갯수 만큼 앞을 먼저 비교
        # 2. n이 0이 아니면 그만큼 뒤에 추가
        
        # if n == 0 :return
        # len1 = len(nums1)
        # end_idx = len1-1
        # while n > 0 and m > 0 :
        #     if nums2[n-1] >= nums1[m-1]:
        #         nums1[end_idx] = nums2[n-1]
        #         n-=1
        #     else:
        #         nums1[end_idx] = nums1[m-1]
        #         m-=1
        #     end_idx-=1
        # while n > 0:
        #     nums1[end_idx] = nums2[n-1]
        #     n-=1
        #     end_idx-=1