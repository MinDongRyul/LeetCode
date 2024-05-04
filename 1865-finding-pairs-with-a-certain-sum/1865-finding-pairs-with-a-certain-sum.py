from collections import Counter

class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = sorted(nums1)
        self.nums2 = nums2

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.nums2[index] += val

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        r = 0
        dic_nums2 = Counter(self.nums2)
        for n in self.nums1:
            if n > tot:
                break
            r += dic_nums2[tot - n]
        return r

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)