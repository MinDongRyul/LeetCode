class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix_sum = 0
        d = {0: 1}

        for i in nums:
            prefix_sum = prefix_sum + i
            # ex) prefix_sum : 28, k : 18인 경우에 d의 key값에 이전까지의 prefix_sum 중 10이 있다면 28 - 10 의 값을 가진 subarray가 존재한다는 것  
            if prefix_sum - k in d:
                # ex) 10의 빈도수 만큼 합산 -> subarray의 수를 구하는게 목표
                result = result + d[prefix_sum - k]

            if prefix_sum not in d:
                d[prefix_sum] = 1
            else:
                d[prefix_sum] = d[prefix_sum] + 1
        
        return result