class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        nums1, nums2 = [],[]
        for idx, num in enumerate(num1[::-1]):
            num = num.ljust(idx+1, '0')
            nums1.append(int(num))
        for idx, num in enumerate(num2[::-1]):
            num = num.ljust(idx+1, '0')
            nums2.append(int(num))
        total = (sum(nums1) + sum(nums2))
        return str(total)