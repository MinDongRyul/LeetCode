class Solution:
    def largestNumber(self, nums):

        # 숫자를 더했을 때 더 크면 True 아니면 False
        # 문자열이어도 '431' > '321' : True
        def compare(a, b):
            return str(a) + str(b) > str(b) + str(a)

        iters = len(nums) - 1
        for i in range(iters):
            wall = iters - i
            # 계속 0~wall까지의 모든 수를 정렬해나감
            for j in range(wall):
                if not compare(nums[j], nums[j + 1]):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return str(int(''.join(map(str, nums))))