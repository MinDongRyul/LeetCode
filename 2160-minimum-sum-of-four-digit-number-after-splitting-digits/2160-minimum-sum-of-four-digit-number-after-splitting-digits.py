class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
#         cnt1, cnt2 = '', ''
#         sorted_num = sorted(str(num))
#         for idx, num in enumerate(sorted_num):
#             if idx % 2 == 0:
#                 cnt1 += num
#             else:
#                 cnt2 += num
#         return int(cnt1) + int(cnt2)

        num = sorted(str(num))
        return int(num[0]) * 10 + int(num[1]) * 10 + int(num[2]) + int(num[3])