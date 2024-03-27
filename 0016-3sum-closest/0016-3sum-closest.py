class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # n^3 과 다를빠 없는 코드
        # nums.sort()
        # min_value = 3001
        # for i in range(len(nums) - 2):
        #     l = i + 1
        #     k = l
        #     r = len(nums) - 1
            
        #     while k < r:
                
        #         while l < r:
        #             total = nums[i] + nums[l] + nums[r]
        #             if min_value >= abs(total - target):
        #                 min_value = abs(total - target)
        #                 re_value = total
        #             print(total, nums[i], nums[l], nums[r])
        #             l += 1
                
        #         r -= 1
        #         k += 1
        #         l = k
        
        # return re_value

        nums.sort()
        # Initialize answer
        answer = nums[0] + nums[1] + nums[2]
        # Iterate the left integer
        for left in range(len(nums) - 2):
            # 2 pointer method on middle and right integers
            middle = left + 1
            right = len(nums) - 1
            while middle < right:
                # Compute guess from 3 pointers
                guess = nums[left] + nums[middle] + nums[right]
                # Update answer if necessary
                if abs(guess - target) < abs(answer - target):
                    answer = guess
                # Guess is too small, increase guess
                if guess < target:
                    middle += 1
                # Guess is too big, decrease guess
                elif guess > target:
                    right -= 1
                # Target found, return it
                # 같은 값은 무조건 정답
                else:
                    return target
            # while 문을 이용해 같은 값을 찾지 못하면(근사값만 찾는다면) 
            # left + 1 해서 비교를 위해 또 다른 근사값을 찾으려함 

        return answer