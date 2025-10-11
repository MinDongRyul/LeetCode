class NumArray:

    def __init__(self, nums: List[int]):
        self.p = [0, nums[0]]
        for num in nums[1:]:
            self.p.append(self.p[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.p[right+1] - self.p[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)