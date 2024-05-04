from collections import Counter

class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = sorted(nums1)
        self.nums2 = nums2
        self.hash2 = Counter(self.nums2)

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.hash2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.hash2[self.nums2[index]] += 1

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        result = 0
        # dic_nums1 = Counter(self.nums1)
        for n in self.nums1:
            if n > tot:
                break
            # r += dic_nums1[key] * dic_nums2[tot - key]
            result += self.hash2[tot - n]
        return result

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)