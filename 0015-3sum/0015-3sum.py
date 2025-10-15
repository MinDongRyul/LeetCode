class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = []
        nums = sorted(nums)

        for i in range(len(nums)-2):
            x, left, right = i, i+1, len(nums)-1

            if nums[i] > 0:
                break
            # 이전과 같으면 패스
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                tot = nums[x] + nums[left] + nums[right]

                if tot > 0:
                    right -= 1
                elif tot < 0:
                    left += 1
                else:
                    answer = [x, nums[left], nums[right]]
                    answers.append(answer)
                    
                    # l이 같은 숫자인게 삽입되는 걸 방지하기 위함
                    while left < right and nums[left] == answer[1]:
                        left += 1
                    # r이 같은 숫자인게 삽입되는 걸 방지하기 위함
                    while left < right and nums[right] == answer[2]:
                        right -= 1
        
        return answers