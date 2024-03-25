class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 틀린 코드 n^3 이라 time limit 발생
        # r = []
        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         for z in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[z] == 0 and sorted([nums[i], nums[j], nums[z]]) not in r:
        #                 r.append(sorted([nums[i], nums[j], nums[z]]))
        # return r

        # 작은 것과 큰것의 위치를 정하기 위함
        nums.sort()
        answer = []
        # 마지막에 2개를 남겨 놓기 위해 len()-2
        for i in range(len(nums) - 2):
            # 정렬되어있기에 nums[i] > 0 이면 0 자체가 sum으로 나올 수 없음 
            if nums[i] > 0:
                break
            # 이전과 같으면 패스
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # i = 0 -> l = 1, r = len() - 1 로 세팅하여 시작
            l = i + 1
            r = len(nums) - 1
            while l < r:
                # 세 개의 sum이 0이 되는지 확인
                total = nums[i] + nums[l] + nums[r]
                # total < 0 이면 i는 고정이고 l는 그 다음 작은 값이기에 늘려줌
                # 정렬상태이기에 가능
                if total < 0:
                    l += 1
                # total > 0 이면 가장 큰 값을 지니고 있는 r 에 대해서 줄여줌
                elif total > 0:
                    r -= 1
                # total = 0 이면 정답 선택  
                else:
                    triplet = [nums[i], nums[l], nums[r]]
                    answer.append(triplet)
                    # l이 같은 숫자인게 삽입되는 걸 방지하기 위함
                    while l < r and nums[l] == triplet[1]:
                        l += 1
                    # r이 같은 숫자인게 삽입되는 걸 방지하기 위함
                    while l < r and nums[r] == triplet[2]:
                        r -= 1
        return answer