class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        # 안쪽의 index
        l = 0
        # 바깥쪽 index
        r = len(height) - 1
        # 바깥쪽 index가 안쪽의 index보다 커지면 종료
        while l < r:
            # 짧은 변이 크기의 높이가 되어짐
            area = (r-l) * min(height[r], height[l])
            # 큰 크기가 정답
            max_area = max(max_area, area)
            # 높이가 낮은 index를 1칸 추가
            # l의 경우는 증가, r의 경우는 감소
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        # 가장 큰 크기 return
        return max_area