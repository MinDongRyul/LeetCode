from collections import deque

class Solution(object):
    def firstUniqChar(self, s):
        
        de=deque(s)

        for _ in range(len(s)):
            a = de.popleft()
            # a 가 de 안에 없으면 반복되지 않는 문자열
            if a not in de:
                return s.index(a)
            # a 가 de에 있으면 반복되는 문자열
            else:
                de.append(a)
                
        # 문자열 길이만큼 돌고 전부다 반복되는 문자열이면 -1 return
        return -1