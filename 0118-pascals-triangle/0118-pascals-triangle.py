class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        final = []
        for i in range(1,numRows+1):
            if i == 1:
                final.append([1])
            elif i == 2:
                final.append([1,1])
            else:
                new_list = []
                for current in range(len(final[-1]) + 1):
                    if current in (0,len(final[-1])):
                        new_list.append(1)
                    else:
                        # 내 위의 왼쪽 값과 내 바로 위 값을 더해서 새로운 값 추정
                        new_list.append(final[-1][current-1]+final[-1][current])
                final.append(new_list)
        return final