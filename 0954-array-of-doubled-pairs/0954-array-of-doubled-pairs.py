from collections import Counter

class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        cnt = Counter(arr)
        arr.sort()
        for x in arr:
            if cnt[x] == 0: continue
            
            # For example: arr=[-5, -2, 1, 2], x = -5, 음수 중 홀수는 2로 나눈 값을 가질 수 없음 
            if x < 0 and x % 2 != 0: return False  
            
            # x가 양수면 2를 곱하고 음수면 2를 나눔
            y = x * 2 if x > 0 else x // 2
            
            # cnt[x]는 있지만 cnt[y]가 이미 끝난경우
            if cnt[y] == 0: return False  
           
            # 위 모든 과정을 거치고나면 x와 그에 해당하는 y를 -1 해줌
            cnt[x] -= 1
            cnt[y] -= 1

        return True