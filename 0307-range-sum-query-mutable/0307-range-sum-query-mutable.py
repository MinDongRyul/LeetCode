def create_tree(lst):
    
    tree = []
    
    for idx, val in enumerate(lst):
        idx += 1

        k = idx & -idx

        if k == 1:
            tree.append(val)
        else:
            tree.append(sum(lst[idx-k:idx]))
        
    return tree

def prefix_sum(i, tree):
    result = 0
    if i > 0:
        while i > 0:
            result += tree[i]
            i -= ((i+1) & -(i+1))
        return result
    elif i == 0:
        return tree[0]

class NumArray(object):
    
    # def __init__(self, nums):
    #     """
    #     :type nums: List[int]
    #     """
    #     self.nums = nums
    #     self.tree = create_tree(nums)
        
    # def update(self, index, val):
    #     """
    #     :type index: int
    #     :type val: int
    #     :rtype: None
    #     """
    #     self.nums[index] = val
    #     self.tree = create_tree(self.nums)

    # def sumRange(self, left, right):
    #     """
    #     :type left: int
    #     :type right: int
    #     :rtype: int
    #     """
    #     if left == 0:
    #         return prefix_sum(right, self.tree)
    #     return prefix_sum(right, self.tree) - prefix_sum(left-1, self.tree)
        
    def __init__(self, nums):
        self.nums = nums
        self.sums = sum(nums)

    def update(self, index, val):
        self.sums += val-self.nums[index]
        self.nums[index] = val

    def sumRange(self, left, right):
        return sum(self.nums[left:right+1]) if right-left < len(self.nums)//2 else self.sums - sum(self.nums[:left]) - sum(self.nums[right+1:])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)