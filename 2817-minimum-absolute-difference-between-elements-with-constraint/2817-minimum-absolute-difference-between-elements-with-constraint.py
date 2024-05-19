import sortedcontainers

class Solution:
    def minAbsoluteDifference(self, nums, x):
        
        # 리스트의 뒤에서부터 시작하며 x만큼의 거리 유지하는 두 포인터 초기화
        j = len(nums) - 1
        i = j - x
        
        # 정렬된 리스트를 유지하기 위해 SortedList 사용
        s = sortedcontainers.SortedList()
        
        # 결과값을 무한대로 초기화
        res = float('inf')
        
        while i >= 0:
            # x 거리 이상 떨어진 새로운 요소를 정렬된 리스트에 추가
            s.add(nums[j])
            
            # 현재 숫자를 정렬된 리스트에 삽입할 수 있는 위치를 찾음
            index = s.bisect_left(nums[i])
            
            # 현재 숫자가 정렬된 리스트에서 가장 작은 값이 아닐 때
            # 왼쪽 위치의 값을 사용하여 결과 업데이트
            if index > 0:
                res = min(res, nums[i] - s[index-1])
                
            # 현재 숫자가 정렬된 리스트에서 가장 큰 값이 아닐 때
            # 오른쪽 위치의 값을 사용하여 결과 업데이트
            if index < len(s):
                res = min(res, s[index] - nums[i])
            
            # i가 0이 될 때까지 반복
            i -= 1
            j -= 1
        
        return res
