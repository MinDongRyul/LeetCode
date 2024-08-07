class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
        sieve = [True] * n

        # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
        m = int(n ** 0.5)
        for i in range(2, m + 1):
            if sieve[i]:           # i가 소수인 경우
                sieve[i * i: n: i] = [False] * len(sieve[i*i: n: i])

        # 소수 목록 산출
        return len([i for i in range(2, n) if sieve[i] == True])